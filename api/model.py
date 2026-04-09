import joblib
import numpy as np
import os

# This works both locally and in Docker
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'final_model.pkl')

model = joblib.load(MODEL_PATH)

def predict_churn(data: dict) -> dict:
    features = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    return {
        'churn_prediction': int(prediction),
        'churn_probability': round(float(probability), 4),
        'risk_level': 'High' if probability > 0.7 else 'Medium' if probability > 0.4 else 'Low'
    }