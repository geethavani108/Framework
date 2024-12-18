
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import joblib
import logging
import mlflow
import mlflow.sklearn

# Configure logging
logging.basicConfig(filename='logs/train_model.log', level=logging.INFO)

def train_model(input_file, model_file):
    try:
        # Load dataset
        df = pd.read_csv(input_file)
        X = df.drop(columns=['HeartDisease'])
        y = df['HeartDisease']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Initialize MLflow experiment
        mlflow.start_run()
        logging.info("MLflow start run executed")
        # Define the model
        model = RandomForestClassifier(random_state=42)
        
        # Hyperparameter tuning
        param_grid = {
            'n_estimators': [5, 10, 20],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
        grid_search.fit(X_train, y_train)
        logging.info("Grid Search fit run executed")
        # Get the best model
        best_model = grid_search.best_estimator_
        
        logging.info("Best model obtained: %s", best_model)
        
        
        # Save the model
        joblib.dump(best_model, model_file)
        logging.info("Mode pickle file is dumped")
        # Evaluate the model
        accuracy = best_model.score(X_test, y_test)
        logging.info("Model training successful with accuracy: %.2f", accuracy)
        
        # Log parameters and metrics to MLflow
        mlflow.log_params(grid_search.best_params_)
        mlflow.log_metric("accuracy", accuracy)
        #mlflow.log_metrics({"cross_val_score_mean": cv_scores.mean(), "cross_val_score_std": cv_scores.std()})
        
        # Log the model to MLflow
        mlflow.sklearn.log_model(best_model, "random_forest_model")

        mlflow.end_run()
        
        return 0

    except Exception as e:
        logging.error("Model training failed: %s", e)
        return 1

if __name__ == "__main__":
  
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    input_file = "data/engineered_data.csv"
    model_file = "data/model.pkl"
    status = train_model(input_file, model_file)
    exit(status)
