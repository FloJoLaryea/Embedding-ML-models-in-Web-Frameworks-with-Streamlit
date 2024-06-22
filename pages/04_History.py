import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title ='History Page',
    
    layout="wide"
)



def display_history_page():
    # get the path of the history data
    csv_path = "./Datasets/prediction_history.csv"
    csv_exists = os.path.exists(csv_path)

    if csv_exists:
        history_data= pd.read_csv(csv_path)
        st.dataframe(history_data)
    else:
        st.write("No history data found")
        st.write("Please run the app and make a prediction to view the history page")
        st.stop()






# st.dataframe(history_df)

if __name__ == "__main__":
    st.title("History Page")
    display_history_page()