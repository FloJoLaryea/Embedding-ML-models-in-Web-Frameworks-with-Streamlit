import streamlit as st 
import pyodbc 
import pandas as pd
import time
from Utils.more_info import markdown_table1
from Utils.more_info import markdown_table2
import streamlit_authenticator as stauth


st.set_page_config(
    page_title= "Data Hub", layout="wide"
)


# Display the app content based on authentication status
if st.session_state['authentication_status']== None:
    st.warning('Please login from the home page')
elif st.session_state['authentication_status'] == False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status']:
    st.title('Customer Churn Database')

   
    train_df = pd.read_csv("./Datasets/Customer_churn_train_data.csv")
    #grouping all numeric columns
    numerics = train_df.select_dtypes("number").columns
    categoricals = train_df.select_dtypes("object").columns


    #create a progress bar to let user know data is loading
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.03)
        progress_bar.progress(perc_completed+1)

    st.success("Data loaded successfully!")

    col1,col2 = st.columns(2)
    with col1:
        option = st.selectbox(
            "How would you like to view data?",
            ("All data", "Numerical columns", "Categorical columns"),
            index=None,
            placeholder="Select view method...",)
       
    # Conditionally display data based on the selected option
    if option == "All data":
        st.write("### All Data")
        st.dataframe(train_df)
        if st.button("Click here to get more information about data dictionary"):
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown_table1)
            with col4:
                st.markdown(markdown_table2)
    elif option == "Numerical columns":
        st.write("### Numerical Columns")
        numerics = train_df.select_dtypes("number").columns
        st.dataframe(train_df[numerics])
        if st.button("Click here to get more information about data dictionary"):
            # Display the markdown table inside the expander
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown_table1)
            with col4:
                st.markdown(markdown_table2)
    elif option == "Categorical columns":
        st.write("### Categorical Columns")
        categoricals = train_df.select_dtypes("object").columns
        st.dataframe(train_df[categoricals])
        if st.button("Click here to get more information about data dictionary"):
            # Display the markdown table inside the expander
            col3,col4 = st.columns(2)
            with col3:
            # Display the markdown table inside the expander
                st.markdown(markdown_table1)
            with col4:
                st.markdown(markdown_table2)





