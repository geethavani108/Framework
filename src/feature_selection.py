import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
import logging

# Configure logging
logging.basicConfig(filename='logs/feature_selection.log', level=logging.INFO)

def select_features(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        X = df.drop(columns=['target'])
        y = df['target']
        selector = SelectKBest(chi2, k=10)
        X_new = selector.fit_transform(X, y)
        selected_features = pd.DataFrame(X_new, columns=X.columns[selector.get_support()])
        selected_features['target'] = y
        selected_features.to_csv(output_file, index=False)
        logging.info("Feature selection successful")
        return 0
    except Exception as e:
        logging.error("Feature selection failed: %s", e)
        return 1

if __name__ == "__main__":
    status = select_features('data/engineered_data.csv', 'data/selected_features.csv')
    exit(status)
