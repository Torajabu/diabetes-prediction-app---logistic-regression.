#  Machine Learning - Diabetes Prediction App

This project is a web-based application that predicts whether a person has diabetes based on various health parameters using a Logistic Regression algorithm.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup & Installation](#setup-installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Docker Hub](#docker-hub)


## Project Overview

This app utilizes a machine learning model trained on the Pima Indians Diabetes Database to predict whether a person is likely to have diabetes based on the following health attributes:

- Number of pregnancies
- Plasma glucose concentration
- Diastolic blood pressure
- Triceps skinfold thickness
- Insulin level
- Body mass index (BMI)
- Diabetes pedigree function
- Age


## Technologies Used

- **Python**: The core programming language.
- **FastAPI**: For building the backend API to handle prediction requests.
- **Streamlit**: For building the interactive frontend.
- **Scikit-learn**: Used for implementing the Logistic Regression model.
- **joblib**: For saving and loading the trained model and scaler.
- **Docker**: For containerization and ease of deployment.
- **Uvicorn**: ASGI server for running FastAPI.

The backend of the application is built using FastAPI for serving the model predictions, and the frontend is built using Streamlit for a user-friendly interface.


## Setup & Installation

### Clone the repository
```bash
git clone https://github.com/Torajabu/diabetes-prediction-app---logistic-regression..git
cd https://github.com/Torajabu/diabetes-prediction-app---logistic-regression..git 
```

## Install dependencies
Create a virtual environment and install the required packages:
```bash
pip install -r requirements.txt
```

## Train the model (if not already done)
Run the following script to train the model:

```bash
python train_model.py
```
This will create the necessary model and scaler files under the models/ directory.

## Run the Application
To run the app locally, use the following command:
```bash
docker build -t diabetes-app .
docker run -p 8000:8000 -p 8501:8501 diabetes-app
```

Once the container is running, open your browser and go to http://localhost:8501 to access the Streamlit frontend.


## Usage
Open the Streamlit app in your browser.

Fill in the details for the health parameters:

Pregnancies: Number of pregnancies (e.g., 6)

Glucose: Plasma glucose concentration (e.g., 5)

Blood Pressure: Diastolic blood pressure (e.g., value)

Skin Thickness: Triceps skinfold thickness (e.g., value)

Insulin: Insulin level (e.g., 2)

BMI: Body mass index (e.g., 0.00)

Diabetes Pedigree Function: Diabetes pedigree function (e.g., 0.00)

Age: Age of the person (e.g., value)

Click the "Predict" button to get the prediction (whether the person is likely to have diabetes or not).

## Model Details
The app uses a Logistic Regression model trained on the [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database).

Logistic Regression is a machine learning algorithm used for binary classification, which is ideal for this problem as it predicts whether a person has diabetes or not (binary output: Diabetes or Not Diabetes).

The model is trained with the following features:

Pregnancies

Glucose level

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age


## Docker Hub
You can also pull the pre-built Docker image from Docker Hub using the following link:

Diabetes Prediction App - Logistic Regression

Simply pull the image and run it as follows:

```bash
docker pull rajab97/diabetespredictionapplogisticregression:latest
docker run -p 8000:8000 -p 8501:8501 rajab97/diabetespredictionapplogisticregression:latest
```

This will run the pre-built application without the need for manual building.
