import os
import streamlit as st
import pandas as pd
import joblib
import datetime
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from catboost import CatBoostClassifier

st.set_page_config(
    page_title ='Predict Page',
    layout="wide"
)
st.title("Predict Churn!")
# load the machine learning model
@st.cache_resource()
def models():
    catboost_model = joblib.load("./ML_models/catboost.joblib")
    log_model = joblib.load("./ML_models/log_regression.joblib")
    sgb_model = joblib.load("./ML_models/sgb_classifier.joblib")
    return catboost_model, log_model,sgb_model


catboost, log_regression,sgb = models()



#model_components = load_ml_components()

# load model components
#catboost_model = model_components["catboost_model"]
#logistic_regressor = model_components["log_regression"]
#sgb_classifier = model_components["sgb_classifier"]

# initialize the session state

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "Catboost" 
# select a model to use
col1,col2 = st.columns(2)
with col1:
    selected_model = st.selectbox("Select model to predict",
                                                 options=["Catboost","Logistic Regression","SGB"],
                                                 key="selected_model",
                                                 index=["Catboost","Logistic Regression","SGB"].index(st.session_state.selected_model))
st.write("#")
# Update the session state based on the selected model
selected_model = st.session_state.selected_model


# select a model from the select_box
@st.cache_resource(show_spinner="loading models...")
def get_selected_model(selected_model):
    if selected_model == "Catboost":
        pipeline =  catboost
    elif selected_model == "Logistic Regression":
        pipeline =  log_regression
    else:
        pipeline =  sgb
    encoder = joblib.load("./ML_models/encoder.joblib")
    return pipeline, encoder


# write a function to make prediction
def make_prediction(pipeline,encoder):
    gender = st.session_state["gender"]
    senior_citizen = st.session_state["senior_citizen"]
    partner = st.session_state["partner"]
    tenure = st.session_state["tenure"]
    monthly_charges = st.session_state["monthly_charges"]
    total_charges = st.session_state["total_charges"]
    payment_method = st.session_state["payment_method"]
    contract = st.session_state["contract"]
    paperless_billing = st.session_state["paperless_billing"]
    dependents = st.session_state["dependents"]
    phone_service = st.session_state["phone_service"]
    multiple_lines = st.session_state["multiple_lines"]
    streaming_tv = st.session_state["streaming_tv"]
    streaming_movies = st.session_state["streaming_movies"]
    online_security = st.session_state["online_security"]
    online_backup = st.session_state["online_backup"]
    device_protection = st.session_state["device_protection"]
    tech_support = st.session_state["tech_support"]
    internet_service = st.session_state["internet_service"]
    
    # create rows for the dataframe
    data=[[gender,senior_citizen,partner,tenure,monthly_charges,total_charges,
           payment_method,contract,paperless_billing,dependents,
           phone_service,multiple_lines,streaming_tv,streaming_movies,
           online_security,online_backup,device_protection,tech_support,
           internet_service]]
    # create columns for the dataframe
    columns = ['gender','senior_citizen','partner','tenure','monthly_charges', 'total_charges'
               ,'payment_method', 'contract','paperless_billing','dependents','phone_service', 
               'multiple_lines','streaming_tv','streaming_movies','online_security', 
               'online_backup', 'device_protection', 'tech_support','internet_service']
    df = pd.DataFrame(data=data,columns=columns)

    # make predictions
    pred = pipeline.predict(df)
    pred_int = int(pred[0])

    # transform the predicted variable 
    prediction = encoder.inverse_transform([[pred_int]])[0]

    # calculate prediction probability
    probability = pipeline.predict_proba(df)[0][pred_int]

     # Map probability to Yes or No
    prediction_label = "Yes" if pred_int == 1 else "No" 

    # update the session state with the prediction and probability
    st.session_state["prediction"] = prediction
    st.session_state["prediction_label"] = prediction_label
    st.session_state["probability"] = probability
    
    # update the dataframe to capture predictions for the history page
    df["PredictionTime"] = datetime.date.today()
    df["ModelUsed"] = st.session_state["selected_model"]
    df["Prediction"] = st.session_state["prediction"]
    df["PredictionProbability"] = st.session_state["probability"]
    # export df as prediction_history.csv
    df.to_csv('./Datasets/prediction_history.csv',mode="a", header=not os.path.exists('./Datasets/prediction_history.csv'),index=False)
    return prediction,prediction_label,probability

# create an 

if "prediction" not in st.session_state:
    st.session_state.prediction = None

if "probability" not in st.session_state:
    st.session_state.probability = None


# write a function to show the forms to accepts input
def display_forms():
    # call the get_selected_model function
    pipeline,encoder = get_selected_model(st.session_state.selected_model)

    with st.form('input-features', clear_on_submit=True):
        col1,col2 = st.columns(2)
        with col1:
            st.write("## Personal Information")
            st.selectbox("Select your gender",options=["Male","Female"],key="gender")
            st.selectbox("Are you a senior citizen?",options=[0,1],key="senior_citizen")
            st.selectbox("Do you have a dependent ?",options=["Yes","No"],key="dependents")
            st.selectbox("Do you have a partner?",options= ["Yes", "No",],key="partner")
            st.number_input("Enter your tenure",min_value = 0, max_value = 72,step=1, key="tenure")
            st.number_input("Enter your monthly charges",min_value=0.00, max_value = 200.00,step=0.10, key="monthly_charges")
            st.number_input("Enter you total charges per year",min_value=0.00,max_value=100000.00, step=0.10,key="total_charges")
            st.selectbox("Select your prefered contract type",options=["Month-to-month","One year","Two year"],key="contract")
            st.selectbox("Select your payment method",options= ["Electronic check", "Mailed check","Bank transfer (automatic)",
        "Credit card (automatic)"], key="payment_method")
        with col2:
            st.write("### Service Information")
            st.selectbox("Do you have a phone service?",options=["Yes","No"],key="phone_service")
            st.selectbox("Do you have a multiple lines?",options=["Yes","No"],key="multiple_lines")
            st.selectbox("Which internet service do you prefer ?",options= ["Fiber optic", "No", "DSL"],key="internet_service")
            st.selectbox("Have you subscribed to our online security service?",options=["Yes","No"],key="online_security")
            st.selectbox("Have you subscribed to our online backup service?",options=["Yes","No"],key="online_backup")
            st.selectbox("Have you subscribed to our device protection service?",options=["Yes","No"],key="device_protection")
            st.selectbox("Have you subscribed to our tech support service?",options=["Yes","No"],key="tech_support")
            st.selectbox("Have you subscribed to our streaming TV service?",options=["Yes","No"],key="streaming_tv")
            st.selectbox("Have you subscribed to our streaming movies service?",options=["Yes","No"],key="streaming_movies")
            st.selectbox("Have you subscribed to our Paperless Billing Service?",options=["Yes","No"],key="paperless_billing")
        st.form_submit_button("Make Prediction",on_click=make_prediction,kwargs=dict(pipeline=pipeline,encoder=encoder))



       

if __name__ == "__main__":
    
    # call the display_forms function
    display_forms()
    #st.write(st.session_state)

    final_prediction = st.session_state["prediction"]
    if not final_prediction:
        st.write("## Prediction shows here")
        st.divider()
    else:
        # display the prediction result result
        col1,col2 = st.columns(2)
        with col1:
            st.write("### Prediction Results")
            st.write(st.session_state["prediction"])
        with col2:
            st.write("### Prediction Probability")
            probability = st.session_state['probability']*100
            st.write(f"{probability:.2f}%")