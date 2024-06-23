import os
import streamlit as st
import pandas as pd
import joblib
import datetime

st.set_page_config(
    page_title ='Bulk Predict Page',
    layout="wide"
)
st.title("Bulk Prediction Page!")

# load the machine learning model components
@st.cache_resource()
def models():
    catboost_model = joblib.load("./ML_models/catboost.joblib")
    log_model = joblib.load("./ML_models/log_regression.joblib")
    sgb_model = joblib.load("./ML_models/sgb_classifier.joblib")
    return catboost_model, log_model,sgb_model

#call the model components
catboost, log_regression,sgb = models()


# Initialize the session state for the model_name
if "model_name" not in st.session_state:
    st.session_state["model_name"] = "CatBoost"

# select the model to use
col1,col2 = st.columns(2)
with col1:
    model_name = st.selectbox("Select Model",options=["CatBoost","Logistic Regression","SGB"],key="model_name")

def values_mapper(df,columns):
    """ This function takes two parameters and map the values in the column
    df: dataframe object
    columns_columns: columnsin in the dataframe that you want to map the values
    returns dataframe
    """
    for col in columns:
        cat_mapping = {True:"Yes",False:"No","No internet service":"No","No phone service":"No"}
        df[col] = df[col].replace(cat_mapping)
    return df

columns_to_map = ["paperless_billing","partner","dependents","phone_service","streaming_movies","streaming_tv","multiple_lines","online_security","online_backup","device_protection","tech_support"]



#function to get selected model
@st.cache_resource()
def get_selected_model():
    if model_name == "CatBoost":
        pipeline = catboost
    elif model_name == "Logistic Regression":
        pipeline = log_regression
    else:
        pipeline = sgb
    
    # load the encoder
    encoder = joblib.load("./ML_models/encoder.joblib")
    return pipeline,encoder


def make_bulk_prediction(pipeline,encoder,data):
    # make prediction
    df = pd.DataFrame(data)
    pred = pipeline.predict(df)
    # decode label to original label in the dataset
    decoded_prediction = encoder.inverse_transform(pred.reshape(-1,1))
    # calculate prediction probability 
    probabbility = pipeline.predict_proba(df)
    # probability_label
    prediction_label = ["Yes" if p == 1 else "No" for p in pred]
    # create a dataframe to store the prediction and probability
    df["PredictionTime"] = datetime.date.today()
    df["Prediction"] = prediction_label
    df["PredictionProbability"] = [probabbility[i][p] for i,p in enumerate(pred)]

    return df


if __name__ == "__main__":
    # call the get_selected_model function
    pipeline,encoder = get_selected_model()
    
    # accept data from user
    uploaded_data = st.file_uploader("Upload your CSV data here for prediction",type="csv")

    if uploaded_data is not None:
        data = pd.read_csv(uploaded_data)

        # drop the churn column
        if "Churn" in data.columns:
            data = data.drop(columns="Churn",axis=1)
        # map the values in the columns
        data = values_mapper(data,columns=columns_to_map)
        # convert TotalCharges to numeric datatype
        data["total_charges"] = pd.to_numeric(data["total_charges"],errors="coerce")
        # map the senior citizen column into Yes or No
        data["senior_citizen"] = data["senior_citizen"].map({0:"No",1:"Yes"})
        # call the make predictions
        prediction_df = make_bulk_prediction(pipeline,encoder,data)
        st.markdown("### View Prediction Result")
        st.write(prediction_df)
    else:
        st.write("Please upload your data")

   