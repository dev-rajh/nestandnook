import streamlit as st

st.title("Welcome to Our Store")

col1, col2 = st.columns(2)

with col1:
    if st.button("🧘 Lifestyle"):
        st.switch_page("pages/Lifestyle.py")

with col2:
    if st.button("🏠 Home Decor"):
        st.switch_page("pages/HomeDecor.py")
