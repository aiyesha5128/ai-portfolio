
import sys
import os
sys.path.append(os.path.abspath("."))

import streamlit as st
from src.care import get_care
st.title("🌿 Plant Identification Agent (MVP)")
st.subheader("Sample Care Lookup")
from src.care import get_care, get_plant_names

plant = st.selectbox(
    "Choose a plant",
    get_plant_names()
)

info = get_care(plant)
if info:
    st.write("### Care Instructions")
    st.write(f"**Light:** {info['light']}")
    st.write(f"**Water:** {info['water']}")
    st.write(f"**Soil:** {info['soil']}")
    st.write(f"**Temperature:** {info['temperature']}")
    st.write(f"**Pet Safety:** {info['pet_safe']}")

