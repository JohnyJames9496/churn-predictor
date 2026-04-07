import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="🔮",
    layout="centered"
)

# Title
st.title(" Customer Churn Predictor")
st.markdown("Fill in customer details to predict churn risk")
st.divider()

# Input form
st.subheader(" Customer Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Has Partner", ["No", "Yes"])
    dependents = st.selectbox("Has Dependents", ["No", "Yes"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    paperless = st.selectbox("Paperless Billing", ["No", "Yes"])

with col2:
    monthly = st.number_input("Monthly Charges ($)", 0.0, 200.0, 65.0)
    total = st.number_input("Total Charges ($)", 0.0, 10000.0, 780.0)
    multiple = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check", 
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])

st.divider()

# Predict button
if st.button(" Predict Churn", use_container_width=True):
    # Build input data
    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": 1 if senior == "Yes" else 0,
        "Partner": 1 if partner == "Yes" else 0,
        "Dependents": 1 if dependents == "Yes" else 0,
        "tenure": tenure,
        "PhoneService": 1 if phone == "Yes" else 0,
        "PaperlessBilling": 1 if paperless == "Yes" else 0,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "MultipleLines_No_phone_service": 1 if multiple == "No phone service" else 0,
        "MultipleLines_Yes": 1 if multiple == "Yes" else 0,
        "InternetService_Fiber_optic": 1 if internet == "Fiber optic" else 0,
        "InternetService_No": 1 if internet == "No" else 0,
        "OnlineSecurity_No_internet_service": 1 if internet == "No" else 0,
        "OnlineSecurity_Yes": 0,
        "OnlineBackup_No_internet_service": 1 if internet == "No" else 0,
        "OnlineBackup_Yes": 0,
        "DeviceProtection_No_internet_service": 1 if internet == "No" else 0,
        "DeviceProtection_Yes": 0,
        "TechSupport_No_internet_service": 1 if internet == "No" else 0,
        "TechSupport_Yes": 0,
        "StreamingTV_No_internet_service": 1 if internet == "No" else 0,
        "StreamingTV_Yes": 0,
        "StreamingMovies_No_internet_service": 1 if internet == "No" else 0,
        "StreamingMovies_Yes": 0,
        "Contract_One_year": 1 if contract == "One year" else 0,
        "Contract_Two_year": 1 if contract == "Two year" else 0,
        "PaymentMethod_Credit_card_automatic": 1 if payment == "Credit card (automatic)" else 0,
        "PaymentMethod_Electronic_check": 1 if payment == "Electronic check" else 0,
        "PaymentMethod_Mailed_check": 1 if payment == "Mailed check" else 0
    }

    # Call FastAPI
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()

        prob = result['churn_probability'] * 100
        risk = result['risk_level']
        prediction = result['churn_prediction']

        st.divider()
        st.subheader(" Prediction Result")

        if risk == "High":
            st.error(f" HIGH RISK — {prob:.1f}% chance of churning!")
            st.warning(" Immediate action recommended — offer retention deal!")
        elif risk == "Medium":
            st.warning(f" MEDIUM RISK — {prob:.1f}% chance of churning")
            st.info(" Consider reaching out with a loyalty offer")
        else:
            st.success(f" LOW RISK — {prob:.1f}% chance of churning")
            st.info(" Customer is likely to stay!")

        # Progress bar
        st.progress(result['churn_probability'])

    except Exception as e:
        st.error(f" Error connecting to API: {e}")
        st.info("Make sure FastAPI is running on port 8000!")