import os
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load the data
data = pd.read_csv(r"C:\CODING\WORKING\data\pima-indians-diabetes-database\diabetes.csv")

# Split features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# Ensure the 'models' directory exists
os.makedirs(r"C:\CODING\WORKING\models", exist_ok=True)

# Save the scaler and model
joblib.dump(scaler, r"C:\CODING\WORKING\models\scaler.joblib")
joblib.dump(model, r"C:\CODING\WORKING\models\logreg_model.joblib")

print("Model and scaler trained and saved successfully!")
