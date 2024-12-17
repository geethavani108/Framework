


import pandas as pd
import requests
import logging
import os

"""

# Ensure the logs directory exists
log_dir = 'logs'
log_file = os.path.join(log_dir, 'data_ingestion.log')

# Create the logs directory if it doesn't exist
try:
    if not os.path.exists(log_dir):
        print("not exists")
        os.makedirs(log_dir, mode = 0o755)
        logging.basicConfig(log_file, level=logging.INFO)
        print(f"Created log directory: {log_dir}")
    else:
        print(f"Log directory already exists: {log_dir}")
except PermissionError as e:
    print(f"Permission error: {e}")
except FileNotFoundError as e:
    print(f"File not found error: {e}")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"Error creating directory: {e}")

# Check if the log file path is correctly set
print(f"Log file path: {log_file}")

# Configure logging
try:
    logging.basicConfig(filename=log_file, level=logging.INFO)
    logging.info('Logging is set up.')
except Exception as e:
    print(f"Error setting up logging: {e}")


"""










# Ensure the logs directory exists 
log_dir = 'logs' 
data_dir  = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir,mode = 0o755)
# Ensure the logs directory exists

if not os.path.exists(log_dir):
    os.makedirs(log_dir,mode = 0o755)


# Configure logging
logging.basicConfig(filename=os.path.join(log_dir, 'data_ingestion.log'), level=logging.INFO)

# Example function to fetch data from a URL and save it as a CSV
def fetch_and_save_csv(url, output_file):
    try:
        logging.info('Fetching data from URL...')
        # Skip bad lines 
        df = pd.read_csv(url, on_bad_lines='skip', sep=',')
        #df = pd.read_csv(url, sep= ',')
        df.to_csv(output_file, index=False)
        logging.info('Data successfully saved to %s', output_file)
    except Exception as e:
        logging.error('Error fetching data: %s', e)
    return 1

if __name__ == "__main__":
    # read a raw file from github 
    url = 'https://raw.githubusercontent.com/geethavani108/DataSets/refs/heads/main/heart.csv'
    output_file = 'data/raw_data.csv'
    status = fetch_and_save_csv(url, output_file)
    logging.info('Data successfully ingested')
    exit(status)

