import streamlit as st
from services.coder import find_icd, find_cpt

st.title("Medical Coding Assistant (ICD-10 + CPT)")

text = st.text_area("Enter Clinical Note")

if st.button("Generate Codes"):

    icd = find_icd(text)
    cpt = find_cpt(text)

    st.subheader("Results")

    if icd:
     st.write("### ICD-10 Codes")
     for item in icd:
            st.write(f"Code: {item['code']}")
            st.write(f"Description: {item['description']}")
            st.write(f"Reason: {item['reason']}")
            st.write("---")
    else:
        st.write("No ICD codes found")
        # CPT OUTPUT
    if cpt:
        st.write("### CPT Codes")
        for item in cpt:
            st.write(f"Code: {item['code']}")
            st.write(f"Description: {item['description']}")
            st.write(f"Reason: {item['reason']}")
            st.write("---")
    else:
        st.write("No CPT codes found")
