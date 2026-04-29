# app.py
import streamlit as st
import pandas as pd
import tempfile
from model import detect_outliers
from utils import plot_feature_hist
from slide_gen import create_presentation
from PIL import Image
import os

st.set_page_config(page_title="Outlier Detector + Slide Generator", layout="centered")
st.title("Outlier Detector + Slide Generator")

uploaded = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.subheader("Data preview")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if not numeric_cols:
        st.error("No numeric columns found. Please upload a CSV with numeric features.")
    else:
        cols = st.multiselect("Select numeric features for outlier detection", numeric_cols, default=numeric_cols[:3])
        cont = st.slider("Contamination (expected fraction of outliers)", min_value=0.01, max_value=0.30, value=0.05, step=0.01)

        if st.button("Run Detection"):
            with st.spinner("Running outlier detection..."):
                res = detect_outliers(df, cols, contamination=cont)

            st.success("Done")
            st.subheader("Sample results (first 10 rows)")
            st.dataframe(res.head(10))

            n_out = int(res['outlier'].sum())
            st.metric("Detected outliers", f"{n_out} / {len(res)}")

            chart_paths = []
            for c in cols[:2]:
                img = plot_feature_hist(res[~res['outlier']], c)
                st.image(img, caption=f"{c} distribution (inliers)")
                tmp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                img.save(tmp.name)
                chart_paths.append(tmp.name)

            summary = f"Outlier detection run on {len(res)} records using features: {', '.join(cols)}. Detected {n_out} outliers."

            out_path = create_presentation("Outlier Report", summary, chart_paths)
            with open(out_path, "rb") as f:
                st.download_button("Download PPTX Report", f, file_name=os.path.basename(out_path))
