import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler,MinMaxScaler


# Configure logging
logging.basicConfig(filename='logs/feature_engineering.log', level=logging.INFO)

def create_features(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        
# Separate the target column
        target = df['HeartDisease']
        features = df.drop(columns=['HeartDisease'])

# Identify numerical and categorical columns
        numerical_features = features.select_dtypes(include=['int64', 'float64']).columns
        categorical_features = features.select_dtypes(include=['object']).columns

# Initialize the scaler
        #scaler = StandardScaler()
        scaler = MinMaxScaler()

# Fit and transform the numerical features
        scaled_numericals = scaler.fit_transform(features[numerical_features])
        logging.info(" Numerical features are scaled")
# Convert the scaled features back to a DataFrame
        scaled_numericals_df = pd.DataFrame(scaled_numericals, columns=numerical_features)

# Extract the categorical features as they are
        categorical_df = features[categorical_features].reset_index(drop=True)

# Combine scaled numerical features and unchanged categorical features
        processed_df = pd.concat([scaled_numericals_df, categorical_df], axis=1)

# Add the target column back to the DataFrame
        final_df = processed_df.copy()
        final_df['HeartDisease'] = target.reset_index(drop=True)
        logging.info("Target  column added successful")

# Display the final DataFrame
        #print(final_df)

        final_df.to_csv(output_file, index=False)
        logging.info("Feature engineering successful")
        return 0
    except Exception as e:
        logging.error("Feature engineering failed: %s", e)
        return 1

if __name__ == "__main__":
    status = create_features('data/processed_data.csv', 'data/engineered_data.csv')
    exit(status)
