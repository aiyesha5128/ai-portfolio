import os
import sys
import streamlit as st

# Add project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

# Project imports
from services.image_identifier_v2 import identify_plant
from services.plant_care_ai import generate_care_guide
from src.care import get_care, get_plant_names

# -----------------------------
# UI Header
# -----------------------------
st.title("🌿 Plant Identification Agent (MVP)")
st.caption("Image-based plant prediction + AI care guide")
st.subheader("Sample Care Lookup")

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a plant image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# If image uploaded → predict plant
if uploaded_file is not None:

    predicted_plant, confidence = identify_plant(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with col2:
        st.success(f"Predicted Plant: {predicted_plant}")
        st.write(f"Confidence: {confidence}")

        # -----------------------------
        # Detect generic / non-plant predictions
        # -----------------------------
        non_plants = ["pot", "flowerpot", "house plant"]

        if any(word in predicted_plant.lower() for word in non_plants):
            st.warning("Exact plant not identified. Showing general care guide.")

            care = generate_care_guide("house plant")
            if care:
                st.subheader("General Plant Care Guide")
                st.markdown(care)

        else:
            # -----------------------------
            # AI-generated care
            # -----------------------------
            care = generate_care_guide(predicted_plant)
            if care:
                st.subheader("AI Care Guide")
                st.markdown(care)

            # -----------------------------
            # Structured care
            # -----------------------------
            info = get_care(predicted_plant)
            if info:
                st.subheader("Care Instructions (Database)")
                st.write(f"**Light:** {info['light']}")
                st.write(f"**Water:** {info['water']}")
                st.write(f"**Soil:** {info['soil']}")
                st.write(f"**Temperature:** {info['temperature']}")
                st.write(f"**Pet Safety:** {info['pet_safe']}")
            else:
                st.warning("No structured care info found for this plant.")