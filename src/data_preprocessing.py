import pandas as pd
import logging

# Configure logging
logging.basicConfig(filename='logs/data_preprocessing.log', level=logging.INFO)

def preprocess_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        df.dropna(inplace=True)
        df['column'] = df['column'].str.lower()
        df.to_csv(output_file, index=False)
        logging.info("Data preprocessing successful")
        return 0
    except Exception as e:
        logging.error("Data preprocessing failed: %s", e)
        return 1

if __name__ == "__main__":
    status = preprocess_data('data/raw_data.csv', 'data/processed_data.csv')
    exit(status)
