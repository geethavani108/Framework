import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='logs/feature_engineering.log', level=logging.INFO)

def create_features(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df['feature_sum'] = df['feature1'] + df['feature2']
        df['feature_ratio'] = df['feature1'] / (df['feature2'] + 1)
        df.to_csv(output_file, index=False)
        logging.info("Feature engineering successful")
        return 0
    except Exception as e:
        logging.error("Feature engineering failed: %s", e)
        return 1

if __name__ == "__main__":
    status = create_features('data/processed_data.csv', 'data/engineered_data.csv')
    exit(status)
