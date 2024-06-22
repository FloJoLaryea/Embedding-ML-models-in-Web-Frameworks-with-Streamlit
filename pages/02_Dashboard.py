import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import altair as alt

st.set_page_config(
    page_title= "Dashboard", layout="wide"
)
# set page theme
alt.themes.enable("dark")
color_map = {"Yes":"blue","No":"green"}
st.title('Customer Churn Dashboard')

train_df_clean = pd.read_csv("./Datasets/Customer_churn_train_data.csv")
numeric_df = train_df_clean.select_dtypes(include=[float, int])


def plot_histograms(df):
    # Get list of all columns
    columns = df.columns
    
    # Create subplots
    fig = go.Figure()
    
    for column in columns:
        fig.add_trace(go.Histogram(x=df[column], name=column))

    # Update layout
    fig.update_layout(
        title_text='Histograms',
        height=1000,  # Set the height to a large value to accommodate multiple subplots
        width=1000,   # Set the width to a large value to accommodate multiple subplots
        barmode='overlay',
        showlegend=False
    )
    
    fig.show()

selected = option_menu(None, options=["KPI", "EDA"], 
     
    menu_icon="cast", default_index=0, orientation="horizontal")
selected
# Conditionally display data based on the selected option
if selected == "EDA":
    col1,col2 = st.columns(2)
    with col1:
        option = st.selectbox(
            "Please choose an option",
            ("Univariate analysis", "Bivariate analysis", "Multivariate analysis"),
            index=None,
            placeholder="Select view method...",)
    # Conditionally display data based on the selected option
    if option == "Univariate analysis":
        st.write("### Univariate analysis")
        col1,col2 = st.columns(2)
        with col1:
            monthlycharges_histogram = px.histogram(train_df_clean,x="monthly_charges",title="Distribution of MonthlyCharges")
            st.plotly_chart(monthlycharges_histogram)
        with col2:
            totalcharges_histgram = px.histogram(train_df_clean,x="total_charges",title="Distribution of TotalCharges")
            st.plotly_chart(totalcharges_histgram)

        col3,col4 = st.columns(2)
        with col3:
        # plot a histogram of Tenure
            tenure_histogram = px.histogram(train_df_clean,x="tenure",title="Distribution of Tenure")
            st.plotly_chart(tenure_histogram)
        with col4:
            pieplot = px.pie(train_df_clean,names="churn",title="churn by internet_service",color="churn",color_discrete_map=color_map,hole=0.3)
            st.plotly_chart(pieplot)
        
        col5,col6 = st.columns(2)
        with col5:
            boxplot = px.box(train_df_clean,x="total_charges",title="BoxPlot of TotalCharges")
            st.plotly_chart(boxplot)
        with col6:
            boxplot = px.box(train_df_clean,x="tenure",title="BoxPlot of Tenure")
            st.plotly_chart(boxplot)

        boxplot = px.box(train_df_clean,x="monthly_charges",title="Boxplot of MonthlyCharges")
        st.plotly_chart(boxplot)

    
        

    if option == "Bivariate analysis":
        st.write("### Bivariate analysis")

        col1,col2 = st.columns(2)
        with col1:
            boxplot = px.box(train_df_clean,x="monthly_charges",y="churn",color="churn",color_discrete_map=color_map,title="Distribution of Churn by MonthlyCharges")
            st.plotly_chart(boxplot)
        with col2:
            boxplot = px.box(train_df_clean,x="total_charges",y="churn",color="churn",color_discrete_map=color_map,title="Distribution of Churn by TotalCharges")
            st.plotly_chart(boxplot)

        col3,col4 = st.columns(2)
        with col3:
            boxplot = px.box(train_df_clean,x="tenure",y="churn",color="churn",color_discrete_map=color_map,title="Distribution of Churn by Tenure")
            st.plotly_chart(boxplot)
        with col4:
            barplot = px.bar(train_df_clean,x="internet_service",y="monthly_charges",color="churn",color_discrete_map=color_map)
            st.plotly_chart(barplot)
            

       
        rows_col = st.columns(2)

        with rows_col[0]:
      
            st.subheader("Correlation matrix")
            corr = train_df_clean.corr(numeric_only=True)
            corr.drop(columns=["Unnamed: 0"],inplace=True)
            #Create a heat map
            fig = go.Figure(data=go.Heatmap(
                z=corr,
                x = corr.columns,
               y= corr.columns))
            fig.update_layout(title="Heatmap")
            st.plotly_chart(fig)

    if option == "Multivariate analysis":
        st.write("### Multivariate analysis")

        col1,col2 = st.columns(2)
        with col1:
            scatter_plot = px.scatter(train_df_clean,x="monthly_charges",y="total_charges",color="churn",color_discrete_map=color_map,title="Relation Between Churn and Charges")
            st.plotly_chart(scatter_plot)
        with col2:
            total_charges_and_tenure = px.scatter(train_df_clean,x="tenure",y="total_charges",color="churn",color_discrete_map=color_map,title="Relationship Between Total Charges and Tenure")
            st.plotly_chart(total_charges_and_tenure)

if selected == "KPI":
    st.markdown(" ### Key Performance Index")
    col1,col2,col3 = st.columns(3)
    with col1: 
        st.markdown(
            f"""
            <div style="background-color: darkturquoise; border-radius:10px; width:80%; margin-top: 20px>
                <h3 style="margin-left:30px">Quick Stats About Dataset</h3>
                <hr>
                <h5 style="margin-left:30px">Churn Rate: {(train_df_clean["churn"].value_counts(normalize=True).get("Yes",0)*100):.2f}%</h5>
                <hr>
                <h5 style="margin-left:30px"> Average Monthly Charges: $ {train_df_clean["monthly_charges"].mean():.2f}</h5>
                <hr>
                <h5 style="margin-left:30px"> Average Yearly Charges: $ {train_df_clean["total_charges"].mean():.2f}</h5>
                <hr>
                <h5 style="margin-left:30px">Number of Customers: {train_df_clean.size}</h5>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        violin_plot = px.violin(train_df_clean,x="churn",y="monthly_charges",title="Impact of Monthly Charges On Customer Churn",color="churn",color_discrete_map=color_map)
        st.plotly_chart(violin_plot)
    with col3:
        churn_by_mu_multipleLiservice = px.bar(train_df_clean,x="multiple_lines",y="monthly_charges",color="churn",color_discrete_map=color_map,title="Churn by Multiple Services and Monthly Charges")
        st.plotly_chart(churn_by_mu_multipleLiservice)

    col4,col5,col6 = st.columns(3)
    with col4:
        churn_by_contract= px.bar(train_df_clean,x="contract",y="monthly_charges",color="churn",color_discrete_map=color_map,title="Churn by Contract Type and Monthly Charges")
        st.plotly_chart(churn_by_contract)
    with col5:
        churn_by_streaming_tv = px.bar(train_df_clean,x="streaming_tv",y="monthly_charges",color="churn",color_discrete_map=color_map,title="Churn by Streaming TV and Monthly Charges")
        st.plotly_chart(churn_by_streaming_tv)
    with col6:
        churn_by_techsupport = px.bar(train_df_clean,x="tech_support",y="monthly_charges",color="churn",color_discrete_map=color_map,title="Churn by Tech Support and Monthly Charges")
        st.plotly_chart(churn_by_techsupport)

    col7,col8,col9 = st.columns(3)
    with col7:
        tenure_versus_charges = px.density_contour(train_df_clean,x="tenure",color="churn",color_discrete_map=color_map,marginal_x="histogram",marginal_y="histogram",title="Tenure by Churn Status")
        st.plotly_chart(tenure_versus_charges)

   