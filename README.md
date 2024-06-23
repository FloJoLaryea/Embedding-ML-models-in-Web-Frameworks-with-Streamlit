
<div align='left'>
  

  <h1>Retention Radar Streamlit App</h1>

  <p>
This is a Streamlit web application for predicting Vodafone Churn. The app uses a trained machine learning model to predict whether a customer is likely to churn or not based on certain input features.
  </p>



<br />


## :signal_strength: Dataset

The trained dataset is originally from the Telco Datasets. The objective is to predict behavior to retain customers by analyzing all relevant customer data and developing focused customer retention programs. It includes following information:

- Customers who left – the column is called Churn
- Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
- Demographic info about customers – gender, age range, and if they have partners and dependents

### Details
- Number of Rows: 5043 (Customers)
- Number of Columns: 21 (Features)
- Class Distribution: (churn value Yes is interpreted as "customer churn")



## :toolbox: Dependecies

`streamlit`

`pandas==2.2.2`

`scikit-learn==1.4.1.post1`

## :gear: Installation

Clone the repository and install the required dependencies using the following commands:

```bash
git clone https://github.com/FloJoLaryea/Embedding-ML-models-in-Web-Frameworks-with-Streamlit.git
```

```bash
cd Embedding-ML-models-in-Web-Frameworks-with-Streamlit
```

```bash
pip install -r requirements-datahub.txt
```

```bash
streamlit run Homepage.py
```

## :play_or_pause_button: Usage

1. Open the app in your web browser and log in.
2. Enter the required information in the input fields.
3. Click the 'Predict' button to generate the prediction.



## :construction: Inputs
Click on the link and reboot the tool or run locally and enter following details such as:

* Tenure (months)
* Phone Service: 0 or 1
* Contract: 0 - Month-to-month, 1 - One year, 2 - Two year
* Paperless Billing: 0 or 1
* Payment Method: 0 - Bank transfer (automatic), 1 - Credit card (automatic), 2 - Electronic check, 3 - Mailed check
* Monthly Charges


## :rocket: Outputs
The app will display following messages:

* "The customer is likely to churn (Yes)." or "The customer is unlikely to churn (No)."
* "The probability of churn is: (X, Y)".



## :triangular_flag_on_post: Deployment and Notebook

This tool has been deployed using render [`Streamlit`](https://streamlit.io/). Checkout the notebook repository [`here`](https://github.com/FloJoLaryea/Embedding-ML-models-in-Web-Frameworks-with-Streamlit).



## :balance_scale: License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Priyanshu88/Telecom-Churn-Prediction-Streamlit-App/blob/main/LICENSE) file for details.



## :handshake: Authors
- Florence Josephina Laryea
- florencelaryea@gmail.com

- [Link to my article on Medium](https://medium.com/@florencelaryea88/retention-radar-app-403283faae84)


### Collaborators

Members of Team Selenium: Bright Abu Kwarteng Snr, Success Makafui Kwawu, Gabriel Kuma.


## 🤗Acknowledgements

Much of our sincere gratitude goes to our instructors Racheal Appiah-Kubi for unwavering support, and invaluable mentorship throughout the course of this project.

Her expertise, dedication, and commitment to our learning journey have been instrumental in shaping our understanding and skills in data analysis
