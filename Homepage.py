#get libraries
import streamlit as st 
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

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
    st.markdown("## Welcome to Retention Radar Pro!")
    col,img_col = st.columns(2)
    with col:
        st.write("---")
        st.markdown(""" #### Every company wants to increase its profit..and retain its customers  - *and we at Selenium Analytics are no different!!* """)
        st.markdown("""
                 #### With our app, you can:
                 - #### Use our powerful machine learning models to predict customer churn without hassle and in real time
                 - #### Make data driven decisions effortlessly""")
        
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
        st.write("#### We are leading professionals with a diverse portfolio range⭐⭐⭐⭐⭐")
        st.markdown("""
                 #### Our group of experts in the team operate with the following objectives:

                 - #### Explore our clients data thoroughly and decide on the most efficient classification models.
                 - #### Find the lifetime value of each customer and know what factors affect the rate at which customers exit a company.
                 - #### Predict if a customer will churn or not.""")
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
        st.title("Explore?")
        st.markdown("""
                    #### We use our three powerful machine learning algorithms models to predict the risk of churn:
                    -  ##### Catboost
                    - ##### Logistic Regression
                    - ##### SQB
                    #### Want to try out with your own dataset? Say less!
                    #### Just upload here in one click!""")
        data_button = st.button("Upload your data",key="data")
        if data_button:
            switch_page("Bulk_Prediction")  


