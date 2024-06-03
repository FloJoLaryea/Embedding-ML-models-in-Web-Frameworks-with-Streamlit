import streamlit as st 

st.set_page_config(
    page_title= "Home Page",layout = 'wide'
)

col1, col2 = st.columns([2,2], gap='small')

col1.markdown("# Customer Churn Analysis")

col1.markdown("### Unveiling the recipe for customer departure")

col2.image('churned.jpg', width = 800)





