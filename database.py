

# def init_connection():
#     return pyodbc.connect(
#         "DRIVER={SQL Server};SERVER="
#         + st.secrets["DBS"]
#         + ";DATABASE="
#         + st.secrets["DBN"]
#         + ";UID="
#         + st.secrets["DBU"]
#         + ";PWD="
#         + st.secrets["DBP"]
#     )

#conn = init_connection()


def running_query(query):
    #with conn.cursor() as c:
       # c.execute(query)
       # rows = c.fetchall()
        #df=pd.DataFrame.from_records(rows, columns=[column[0] for column in c.description])
    #return df

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
    #second_train = pd.read_csv(second_dataset_path)
    
    # Concatenate the two DataFrames
    #train_df = pd.concat([first_train, second_train], ignore_index=True)
    
    return first_train

#train_df = load_and_concat_datasets(get_all_columns, "./Datasets/LP2_Telco-churn-second-2000.csv")


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

