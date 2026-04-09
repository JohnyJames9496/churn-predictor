# Customer Churn Prediction System

A production-grade Machine Learning system that predicts whether a telecom customer will churn or not. Built with Python, Scikit-learn, FastAPI, Streamlit and Docker.

---

## What This Project Does

Telecom companies lose millions when customers leave. This system predicts which customers are likely to churn so the company can take action before losing them. The user fills in customer details in a web form and instantly gets a churn risk prediction with probability score.

---

## Tech Stack

Language: Python 3.10
ML Libraries: Scikit-learn, XGBoost, Imbalanced-learn
Data Processing: Pandas, NumPy
Backend API: FastAPI
Frontend: Streamlit
Deployment: Docker and Docker Compose
Version Control: Git and GitHub

---

## Model Performance After SMOTE

Accuracy: 76.19%
Precision: 54.30%
Recall: 65.78%
F1 Score: 59.49%
ROC-AUC: 80.99%

Logistic Regression was selected as the final model based on best ROC-AUC and F1 Score among four models tested including Logistic Regression, Decision Tree, Random Forest and XGBoost.

---

## ML Pipeline

1. Data Collection — Telco Customer Churn dataset with 7043 customers and 21 features
2. Data Cleaning — Fixed TotalCharges column, handled 11 missing values
3. Feature Engineering — Binary encoding and one-hot encoding of 15 categorical columns
4. Model Training — Trained and compared 4 ML models
5. Class Imbalance — Applied SMOTE to balance churners and non-churners
6. Evaluation — Confusion Matrix, ROC Curve, Accuracy, Precision, Recall, F1, ROC-AUC
7. Deployment — FastAPI backend, Streamlit frontend, fully Dockerized

---

## Key Decisions and Why

Logistic Regression was chosen because it had the best ROC-AUC score of 0.8286 and best F1 Score of 0.5546 among all models tested. SMOTE was applied only on training data to avoid data leakage. Recall was prioritized over Precision because missing an actual churner costs the business more than a false alarm. FastAPI was chosen for its speed and automatic Swagger documentation. Docker was used so the project runs consistently on any machine with a single command.

---

## Project Structure

churn-predictor/
├── data/
│   ├── telco_churn.csv
│   └── telco_churn_cleaned.csv
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_improved_model.ipynb
├── models/
│   ├── final_model.pkl
│   ├── model_comparison.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
├── api/
│   ├── main.py
│   ├── model.py
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   └── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

---

## Dataset

Telco Customer Churn Dataset from Kaggle
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
7043 customers, 21 features, binary classification — Churn or No Churn

---
