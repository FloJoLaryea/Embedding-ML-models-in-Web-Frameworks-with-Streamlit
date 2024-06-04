#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie

#set page configuration
st.set_page_config(
    page_title= "Home Page",layout = 'wide'
)

#define function to get animation
def lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_img = lottie_url("https://lottie.host/80d6a368-c787-4f59-8eca-9b649cf41b1b/VdfzfJeXsp.json")


#intro talking about title 
with st.container():
    st.title("Unveiling secrets contributing to customer churn")
    st.write("##")
    st.write("""Every company wants to increase its profit or revenue margin and customer retention is one key area industry players 
             focus their resources - and we at Vodafone are no different!!""")
with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.header("About us")
        st.write("##")
        st.write("""
                 Our group of experts in the team operate with the following objectives:

                 - Explore our clients data thoroughly and decide on the most efficient classification models.
                 - Find the lifetime value of each customer and know what factors affect the rate at which customers stop using their network.
                 - Predict if a customer will churn or not.""")
    with col2:
        st_lottie(
    lottie_img,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=500,
    width=600

)

with st.container():
        st.write("---")
        st.header("Explore")
        st.write("##")
        st.write("With our powerful machine learning algorithms, you could also try to predict whether a customer will churn or not with you own dataset!")
        uploaded_file = st.file_uploader("Upload your file here")



