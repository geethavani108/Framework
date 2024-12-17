import pandas as pd
import logging
import os
from sklearn.preprocessing import LabelEncoder


log_dir = 'logs' 
data_dir  = 'data'
if not os.path.exists(log_dir):
    os.makedirs(log_dir,mode = 0o755)
if not os.path.exists(data_dir):
    os.makedirs(log_dir,mode = 0o755)



# Configure logging
logging.basicConfig(filename=os.path.join(log_dir, 'data_preprocessing.log'), level=logging.INFO)

# Configure logging
#logging.basicConfig(filename='logs/data_preprocessing.log', level=logging.INFO)
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def preprocess_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        #df =sf.drop(columns=['HeartDisease'],inplace=False)
        #df.drop(columns=['repair_type'], inplace=True)

        #******************************************
   

        # Encode categorical variables
        categorical_columns = df.select_dtypes(include=["object"]).columns
        label_encoders = {}
        for column in categorical_columns:
            le = LabelEncoder()
            df[column] = le.fit_transform(df[column])
            label_encoders[column] = le
        logging.info("Encoding all categorical columns successful")

        #******************************************************

    # Remove rows where RestingBP or Cholesterol are 0
        df = df[(df['RestingBP'] != 0) & (df['Cholesterol'] != 0)]

    # there are many outliers in RestingBP and Cholestrol
    # Function to remove outliers using IQR

    # Remove outliers from RestingBP and Cholesterol
        df = remove_outliers_iqr(df, 'RestingBP')
        df = remove_outliers_iqr(df, 'Cholesterol')
        logging.info("Checked Outliers and removed for Resting BP and cholesterol successful")
        #df['column'] = df['column'].str.lower()
        df.to_csv(output_file, index=False)
        logging.info("Data preprocessing successful")
        return 0
    except Exception as e:
        logging.error("Data preprocessing failed: %s", e)
        return 1

if __name__ == "__main__":
    status = preprocess_data('data/raw_data.csv', 'data/processed_data.csv')
    exit(status)
