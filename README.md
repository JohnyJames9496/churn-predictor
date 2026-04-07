# Customer Churn Prediction System

A production-grade Machine Learning system that predicts whether a telecom customer will churn or not.

Built with Python, Scikit-learn, FastAPI, and Streamlit.

---

## Project Overview

Customer churn is when a customer stops using a company's service.
This system helps telecom companies identify high-risk customers
before they leave, so they can take action and retain them.

---
---

## ML Pipeline

1. Data Collection — Telco Customer Churn dataset (7043 customers)
2. Data Cleaning — Fixed TotalCharges, handled missing values
3. Feature Engineering — One-hot encoding, binary encoding
4. Model Training — Trained 4 models and compared
5. Class Imbalance — Applied SMOTE to improve Recall
6. Evaluation — Confusion Matrix, ROC Curve, F1 Score
7. Deployment — FastAPI + Streamlit + Docker

---

## Key Decisions and Why

- Logistic Regression chosen for best ROC-AUC and F1 Score
- SMOTE applied to improve Recall from 50% to 66%
- Recall prioritized because missing a churner costs more than a false alarm
- FastAPI used for automatic Swagger documentation
- Docker used for consistent deployment across environments

---

