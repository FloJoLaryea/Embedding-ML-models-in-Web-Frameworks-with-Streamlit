import streamlit as st 
import pyodbc 
import pandas as pd
import time

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

first_train = get_all_columns()

second_train = pd.read_csv("./Datasets/LP2_Telco-churn-second-2000.csv")

train_df = pd.concat([first_train,second_train])

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
    time.sleep(0.05)
    progress_bar.progress(perc_completed+1)

st.success("Data loaded successfully!")



#grouping all numeric columns
numerics = train_df.select_dtypes("number").columns
#grouping all categorical columns
categoricals = train_df.select_dtypes("object").columns

option = st.selectbox(
    "How would you like to view data?",
    ("All data", "Numerical columns", "Categorical columns"),
    index=None,
    placeholder="Select contact method...",)
# Conditionally display data based on the selected option
if option == "All data":
    st.write("### All Data")
    st.dataframe(train_df)
elif option == "Numerical columns":
    st.write("### Numerical Columns")
    st.dataframe(train_df[numerics])
elif option == "Categorical columns":
    st.write("### Categorical Columns")
    st.dataframe(train_df[categoricals])


markdown_table = """
| Column Names|Description| Data Type|
|-------------|-----------|----------|
|Gender|Whether the customer is a male or a female|object|
|SeniorCitizen|Whether a customer is a senior citizen or not|int64|
|Partner|Whether the customer has a partner or not (Yes, No)|object|
|Dependents|Whether the customer has dependents or not (Yes, No)|object|
|Tenure|Number of months the customer has stayed with the company|int64|
|Phone Service|Whether the customer has a phone service or not (Yes, No)|object|
|MultipleLines|Whether the customer has multiple lines or not|object|
|InternetService|Customer's internet service provider (DSL, Fiber Optic, No)|object|
|OnlineSecurity|Whether the customer has online security or not (Yes, No, No Internet)|object|
|OnlineBackup|Whether the customer has online backup or not (Yes, No, No Internet)|object|
|DeviceProtection|Whether the customer has device protection or not (Yes, No, No internet service)|object|
|TechSupport|Whether the customer has tech support or not (Yes, No, No internet)|object|
|StreamingTV|Whether the customer has streaming TV or not (Yes, No, No internet service)|object|
|StreamingMovies|Whether the customer has streaming movies or not (Yes, No, No Internet service)|object|
|Contract|The contract term of the customer (Month-to-Month, One year, Two year)|object|
|PaperlessBilling|Whether the customer has paperless billing or not (Yes, No)|object|
|Payment Method|The customer's payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))|object|
|MonthlyCharges|The amount charged to the customer monthly|float64|
|TotalCharges|The total amount charged to the customer|float64|
|Churn|Whether the customer churned or not (Yes or No)|object| 
"""

if st.button("Click here "):
     # Display the markdown table inside the expander
    st.markdown(markdown_table)



