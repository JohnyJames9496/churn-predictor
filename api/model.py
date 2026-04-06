import joblib
import numpy as np

#Load the trained model once when API starts
model = joblib.load('../models/final_model.pkl')

def predict_churn(data: dict) -> dict:
  #convert input data to array
  features = np.array(list(data.values())).reshape(1, -1)
  
  #Get prediction and probability

  prediction = model.predict(features)[0]
  probability = model.predict_proba(features)[0][1] 

  return {
    'churn_prediction': int(prediction),
    'churn_probability': float(probability),
    'risk_level': 'High' if probability > 0.7 else 'Medium' if probability > 0.4 else 'Low'
  }    