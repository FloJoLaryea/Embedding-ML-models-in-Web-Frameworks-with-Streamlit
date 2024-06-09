import streamlit as st 
import pyodbc 
import pandas as pd
import time
from Utils.more_info import markdown_table1
from Utils.more_info import markdown_table2

st.set_page_config(
    page_title= "Data Hub", layout="wide"
)

st.title('Customer Churn Analysis')


@st.cache_resource(show_spinner='Please wait for a second...')

def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets["DBS"]
        + ";DATABASE="
        + st.secrets["DBN"]
        + ";UID="
        + st.secrets["DBU"]
        + ";PWD="
        + st.secrets["DBP"]
    )

conn = init_connection()


@st.cache_data(show_spinner='Loading data, This will only take a minute..')
def running_query(query):
    with conn.cursor() as c:
        c.execute(query)
        rows = c.fetchall()
        df=pd.DataFrame.from_records(rows, columns=[column[0] for column in c.description])
    return df

def get_all_columns():
    sql_query = 'SELECT * FROM dbo.LP2_Telco_churn_first_3000'
    df = running_query(sql_query)
    return df


def load_and_concat_datasets(first_dataset_func, second_dataset_path):
    """
    Load the first dataset using a provided function and the second dataset from a CSV file,
    then concatenate them into a single DataFrame.
    
    Parameters:
    - first_dataset_func: function that returns a DataFrame for the first dataset.
    - second_dataset_path: string path to the second dataset CSV file.
    
    Returns:
    - A concatenated DataFrame containing both datasets.
    """
    # Load the first dataset using the provided function
    first_train = first_dataset_func()
    
    # Load the second dataset from the provided CSV file path
    second_train = pd.read_csv(second_dataset_path)
    
    # Concatenate the two DataFrames
    train_df = pd.concat([first_train, second_train], ignore_index=True)
    
    return train_df

train_df = load_and_concat_datasets(get_all_columns, "./Datasets/LP2_Telco-churn-second-2000.csv")


# Define a dictionary for mapping boolean and None values to more meaningful categories
new_cat_values_mapping = {
    'multiple_lines': {True: 'Yes', False: 'No', None: 'No phone service'},
    'online_security': {True: 'Yes', False: 'No', None: 'No internet service'},
    'online_backup': {True: 'Yes', False: 'No', None: 'No internet service'},
    'device_protection': {True: 'Yes', False: 'No', None: 'No internet service'},
    'tech_support': {True: 'Yes', False: 'No', None: 'No internet service'},
    'streaming_tv': {True: 'Yes', False: 'No', None: 'No internet service'},
    'streaming_movies': {True: 'Yes', False: 'No', None: 'No internet service'},
    'churn': {True: 'Yes', False: 'No', None: 'No'},
    'partner': {True: 'Yes', False: 'No'},
    'dependents': {True: 'Yes', False: 'No'},
    'paperless_billing': {True: 'Yes', False: 'No'},
    'phone_service': {True: 'Yes', False: 'No'},
}

# Replace old categories with the new ones
train_df.replace(new_cat_values_mapping, inplace=True)


#create a progress bar to let user know data is loading
progress_bar = st.progress(0)
for perc_completed in range(100):
    time.sleep(0.03)
    progress_bar.progress(perc_completed+1)

st.success("Data loaded successfully!")



#grouping all numeric columns
numerics = train_df.select_dtypes("number").columns
#grouping all categorical columns
categoricals = train_df.select_dtypes("object").columns

col1,col2 = st.columns(2)
with col1:
    option = st.selectbox(
        "How would you like to view data?",
        ("All data", "Numerical columns", "Categorical columns"),
        index=None,
        placeholder="Select contact method...",)
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
    st.dataframe(train_df[categoricals])
    if st.button("Click here to get more information about data dictionary"):
        # Display the markdown table inside the expander
        col3,col4 = st.columns(2)
        with col3:
        # Display the markdown table inside the expander
            st.markdown(markdown_table1)
        with col4:
            st.markdown(markdown_table2)





