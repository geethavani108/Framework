import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import logging

# Configure logging
logging.basicConfig(filename='logs/train_model.log', level=logging.INFO)

def train_model(input_file, model_file):
    try:
        df = pd.read_csv(input_file)
        X = df.drop(columns=['target'])
        y = df['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        joblib.dump(model, model_file)
        accuracy = model.score(X_test, y_test)
        logging.info("Model training successful with accuracy: %.2f", accuracy)
        return 0
