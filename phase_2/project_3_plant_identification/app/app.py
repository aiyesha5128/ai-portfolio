import sys
import os

# Add the project root to Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)



import streamlit as st

from services.local_image_identifier import identify_plant
from services.plant_care_ai import get_care_guide  # keep the same function signature



st.title("Plant Identifier & Care Guide")

uploaded_file = st.file_uploader("Upload a plant image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    with st.spinner("Identifying plant..."):
        predictions = identify_plant(uploaded_file)
    
    if predictions:
        st.subheader("Top Predictions")
        for i, pred in enumerate(predictions[:3], 1):
            st.write(f"{i}. {pred['name']} — Confidence: {pred['score']*100:.1f}%")
        
        # Keep existing argument name for plant_care.py
        plant_name = predictions[0]['name']  
        care_info = get_care_guide(plant_name)
        
        st.subheader(f"Care Guide for {plant_name}")
        st.write(care_info)
    else:
        st.write("Could not identify the plant. Try another image.")