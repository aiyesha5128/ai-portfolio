import streamlit as st
from services.coder import find_icd, find_cpt

st.title("Medical Coding Assistant (ICD-10 + CPT)")

note = st.text_area("Enter Clinical Note")

if st.button("Generate Codes"):

    icd = find_icd(note)
    cpt = find_cpt(note)

    st.subheader("Results")

    if icd:
        st.write("### ICD-10")
        st.write(f"Code: {icd['code']}")
        st.write(f"Description: {icd['description']}")
        st.write(f"Reason: {icd['reason']}")
    else:
        st.write("No ICD code found")

    if cpt:
        st.write("### CPT")
        st.write(f"Code: {cpt['code']}")
        st.write(f"Description: {cpt['description']}")
        st.write(f"Reason: {cpt['reason']}")
    else:
        st.write("No CPT code found")