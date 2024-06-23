#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

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

lottie_home = lottie_url("https://lottie.host/56f1fdb0-7195-4d5e-ab49-1beb911cc968/GZnG6lXfIu.json")

selected = option_menu(None, options=["Home", "About Us", "Upload"], 
    icons=['house','gear', 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected
#intro talking about title 
if selected == "Home":
    st.title("Unveiling secrets contributing to customer churn")
    st.write("##")
    col,img_col = st.columns(2)
    with col:
        st.markdown("## Welcome to Retention Radar Pro!")
        st.write("---")
        st.markdown("""Every company wants to increase its profit or revenue margin and customer retention is one key area industry players 
             focus their resources - **and we at Selenium Analytics are no different!!**""")
        st.write("We are leading professionals with a diverse portfolio range⭐⭐⭐⭐⭐")
        st.write("""
                 On our page, you can:
                 - Test our powerful machine learning algorithms to predict a customer churning
                 - Even include your own dataset""")
        
    with img_col:
          st_lottie(
    lottie_img,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=300,
    width=600
          )
         
if selected == "About Us":
    col1, col2 = st.columns(2)
    with col1:
        st.title("About us")
        st.write("##")
        st.write("""
                 Our group of experts in the team operate with the following objectives:

                 - Explore our clients data thoroughly and decide on the most efficient classification models.
                 - Find the lifetime value of each customer and know what factors affect the rate at which customers stop using their network.
                 - Predict if a customer will churn or not.""")
    with col2:
        st_lottie(
    lottie_home,
    speed=1,
    reverse= False,
    loop=True,
    quality="high",
    key="coding",
    height=500,
    width=600

)

if selected == "Upload":
        st.title("Explore")
        
        st.markdown("""
                    ### With our three powerful machine learning algorithms trained with , you could also try to predict 
                    ### whether a customer will churn or not with you own dataset!""")
      
        st.write("We use:")
        st.markdown("""
                    -  Catboost
                    - Logistic Regression
                    - SQB""")
        uploaded_file = st.file_uploader("Upload your file here")
        st.markdown("*Good to remember : Please rename your corresponding columns to match ours*")



