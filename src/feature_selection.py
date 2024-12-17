import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
import logging
#Use a RandomForest classifier to compute feature importance scores.
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
# Configure logging
logging.basicConfig(filename='logs/feature_selection.log', level=logging.INFO)






def select_features(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        X = df.drop(columns=['HeartDisease'])
        y = df['HeartDisease']
        #  Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# Define the model
#3. Feature Importance with RandomForest
#---------------------------------
        model = RandomForestClassifier(random_state=42)

# Fit the model
        model.fit(X_train, y_train)

# Get feature importances
        importances = model.feature_importances_
        
# Create a DataFrame for feature importances
        feature_importances = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
        })
        # Sort the DataFrame by importance
        feature_importances = feature_importances.sort_values(by='Importance', ascending=False)
        logging.info("Method :3 Feature importances:")
        logging.info(feature_importances)


        feature_importances.to_csv(output_file, index=False)
        logging.info("Feature selection successful")
        return 0
    except Exception as e:
        logging.error("Feature selection failed: %s", e)
        return 1

if __name__ == "__main__":
    status = select_features('data/engineered_data.csv', 'data/selected_features.csv')
    exit(status)
