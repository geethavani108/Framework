import subprocess

def run_pipeline():
     # Run data ingertion
    #subprocess.run(['python', 'src/data_ingestion.py'])
    # Run data preprocessing
    #subprocess.run(['python', 'src/data_preprocessing.py'])
    
    # Run feature engineering
    #subprocess.run(['python', 'src/feature_engineering.py'])
    
    # Run feature selection
    subprocess.run(['python', 'src/feature_selection.py'])
    
    # Run model training
    #subprocess.run(['python', 'src/train_model.py'])
    
    # Run model deployment
    #subprocess.run(['python', 'src/deploy_model.py'])

if __name__ == "__main__":
    run_pipeline()
