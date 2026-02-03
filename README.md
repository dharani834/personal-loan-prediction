# 🏦 Bank Personal Loan Prediction using Machine Learning

## 📍 Project Overview
This project predicts whether a bank customer is likely to **accept a personal loan offer** based on customer details such as income, education, family size, credit card usage, mortgage, and other factors.  
The goal is to help banks identify potential customers for loan marketing and improve decision-making.

---

## 🎯 Objective
To build a Machine Learning model that can classify customers into:
- ✅ **Loan Accepted**
- ❌ **Loan Not Accepted**

---

## 📂 Dataset
**File:** `Bank_Personal_Loan_Modelling(1).csv`  
The dataset contains customer information like:
- Age  
- Income  
- Family  
- Education  
- Mortgage  
- Credit Card Average Spending (CCAvg)  
- Online usage, etc.

**Target Column:** `Personal Loan` (Yes/No)

---

## 🔍 Project Workflow
### 1️⃣ Data Preprocessing
- Checked and handled missing values
- Converted categorical features into numerical format
- Selected important features for model training

### 2️⃣ Exploratory Data Analysis (EDA)
- Analyzed relationships between customer attributes and loan acceptance
- Identified key factors affecting loan approval

### 3️⃣ Model Training
- Built a classification model using Machine Learning algorithms
- Trained the model and evaluated performance

### 4️⃣ Model Saving
- Saved the trained model as `loan_model.pkl` for reuse

### 5️⃣ Deployment
- Developed a **Streamlit web app** (`app.py`) for real-time predictions
- Users can enter customer details and get instant prediction results

---

## 🧠 Machine Learning Model
- Model Type: **Classification**
- Algorithm Used: *(Example: Balanced Random Forest Classifier / Random Forest)*  
- Evaluation Metrics:
  - Accuracy
  - Confusion Matrix
  - Precision / Recall / F1-score

---

## 🖥️ Streamlit App Features
✅ User-friendly input form  
✅ Predict loan acceptance instantly  
✅ Shows result as **Accepted / Not Accepted**

---

## ▶️ How to Run the Project Locally

### Step 1: Clone the repository
```bash
git clone <https://github.com/dharani834/personal-loan-prediction.git>
cd <personal-loan-prediction>
###Step 2: Install required libraries
pip install -r requirements.txt
###Step 3: Run the Streamlit app
streamlit run app.py
Step 4: Open in browser
http://localhost:8501
