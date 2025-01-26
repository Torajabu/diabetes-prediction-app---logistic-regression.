from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the logistic regression model and scaler
# if linux or from docker use model = joblib.load("/models/logreg_model.joblib")
# scaler = joblib.load("/models/scaler.joblib")
model = joblib.load(r"C:\CODING\WORKING\models\logreg_model.joblib")
scaler = joblib.load(r"C:\CODING\WORKING\models\scaler.joblib")

# Define the input data model
class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Initialize FastAPI app
app = FastAPI()

# Define prediction endpoint
@app.post("/predict")
def predict(data: DiabetesData):
    try:
        # Prepare input data as a DataFrame
        input_data = {
            'Pregnancies': [data.Pregnancies],
            'Glucose': [data.Glucose],
            'BloodPressure': [data.BloodPressure],
            'SkinThickness': [data.SkinThickness],
            'Insulin': [data.Insulin],
            'BMI': [data.BMI],
            'DiabetesPedigreeFunction': [data.DiabetesPedigreeFunction],
            'Age': [data.Age]
        }
        input_df = pd.DataFrame(input_data)

        # Scale the input data
        scaled_data = scaler.transform(input_df)

        # Make a prediction
        prediction = model.predict(scaled_data)
        result = "Diabetes" if prediction[0] == 1 else "Not Diabetes"

        return {"prediction": result}

    except Exception as e:
        return {"error": str(e)}
