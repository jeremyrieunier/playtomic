import streamlit as st

st.set_page_config(
    page_title="Hola Playtomic",
    page_icon="👋",
)

st.title("👋 Hola Playtomic")

st.markdown(
    """
    Soy Jeremy. Here you'll find my answers for the Product Data Analyst position case study.
   
    ### Take-home assignments
"""
)

st.page_link("pages/1_SQL.py", label="SQL exercises", icon="📊")
st.page_link("pages/2_Product_Analytics.py", label="A/B Testing & Product Analytics", icon="🧪")
st.page_link("pages/3_Forecasting.py", label="Forecasting with Prophet", icon="📈")

st.markdown("---")
st.markdown("Made using Streamlit. Code is on [Github](https://github.com/jeremyrieunier/playtomic). And this is mon [Linkedin profile](https://www.linkedin.com/in/jeremyrieunier/).")