import os
import sys
import streamlit as st

# Add project root to Python path (so "services" and "src" can be imported)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from services.image_identifier_v1 import identify_plant
from src.care import get_care, get_plant_names
# Ensure imports work when running from project root
sys.path.append(os.path.abspath("."))

# -----------------------------
# UI Header
# -----------------------------
st.title("🌿 Plant Identification Agent (MVP)")
st.caption("MVP — JSON-based prediction (Vision API integration coming next)")
st.subheader("Sample Care Lookup")

# -----------------------------
# Upload Image
# -----------------------------
predicted_plant = None
confidence = None

uploaded_file = st.file_uploader(
    "Upload a plant image",
    type=["jpg", "jpeg", "png"]
)

# If user uploads an image, predict plant and show preview
if uploaded_file is not None:
    predicted_plant, confidence = identify_plant(uploaded_file)

    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success(f"Predicted Plant: {predicted_plant}")
    st.write(f"Confidence: {confidence}")

# -----------------------------
# Choose plant name to show care
# -----------------------------
if predicted_plant:
    st.info(f"Using predicted plant: **{predicted_plant}**")
    plant_name = predicted_plant
else:
    plant_name = st.selectbox("Choose a plant (manual selection)", get_plant_names())

# -----------------------------
# Show care instructions
# -----------------------------
info = get_care(plant_name)

if info:
    st.write("### Care Instructions")
    st.write(f"**Light:** {info['light']}")
    st.write(f"**Water:** {info['water']}")
    st.write(f"**Soil:** {info['soil']}")
    st.write(f"**Temperature:** {info['temperature']}")
    st.write(f"**Pet Safety:** {info['pet_safe']}")
else:
    st.warning("No care info found for this plant.")