import streamlit as st
import pickle
import numpy as np

# Title
st.title("💰 Bank Personal Loan Prediction")

# Load trained model
model = pickle.load(open("loan_model.pkl", "rb"))

# Sidebar / input fields
st.sidebar.header("Customer Information")
age = st.sidebar.number_input("Age", 18, 70, 30)
experience = st.sidebar.number_input("Experience (Years)", 0, 50, 5)
income = st.sidebar.number_input("Annual Income ($000)", 0, 500, 50)
family = st.sidebar.number_input("Family Size", 1, 5, 2)
ccavg = st.sidebar.number_input("Avg. Credit Card Spending", 0.0, 10.0, 1.5)
education = st.sidebar.selectbox("Education Level", [1, 2, 3])  # 1=Undergrad, 2=Graduate, 3=Advanced
mortgage = st.sidebar.number_input("Mortgage Value ($000)", 0, 700, 0)
securities = st.sidebar.selectbox("Securities Account", [0, 1])
cd_account = st.sidebar.selectbox("CD Account", [0, 1])
online = st.sidebar.selectbox("Online Banking", [0, 1])
creditcard = st.sidebar.selectbox("Credit Card User", [0, 1])

# Prepare features
features = np.array([[age, experience, income, family, ccavg, education, mortgage,
                      securities, cd_account, online, creditcard]])

# Prediction button
if st.button("Predict Loan Eligibility"):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ Customer is likely to ACCEPT the Personal Loan")
    else:
        st.error("❌ Customer is NOT likely to accept the Personal Loan")
