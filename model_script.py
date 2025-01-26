import joblib
import numpy as np
import pandas as pd

# Load your trained model
model = joblib.load('model.pkl')

# Define a function for inference
def predict(file_path):
    # Read the file into a DataFrame
    df = pd.read_csv(file_path)
    #df = preprocess_features(df)
    return model.predict(df)

# Preprocess the features as needed (example)
def preprocess_features(df):
    # Example preprocessing steps
    df["Sex"] = df["Sex"].map({"M": 0, "F": 1})
    df["ChestPainType"] = df["ChestPainType"].map({"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3})
    df["ExerciseAngina"] = df["ExerciseAngina"].map({"N": 0, "Y": 1})
    df["ST_Slope"] = df["ST_Slope"].map({"Up": 0, "Flat": 1, "Down": 2})
    # Add more preprocessing steps as per your model requirements
    return df

# Example usage
if __name__ == "__main__":
    # Replace with your file path
    file_path = 'test_data.csv'
    predictions = predict(file_path)
    print(f'Predictions: {predictions}')
