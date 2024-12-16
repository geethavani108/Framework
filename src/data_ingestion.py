import requests
import logging

# Configure logging
logging.basicConfig(filename='logs/data_ingestion.log', level=logging.INFO)

def fetch_data(api_url, file_path):
    try:
        response = requests.get(api_url)
        data = response.json()
        with open(file_path, 'w') as file:
            json.dump(data, file)
        logging.info("Data ingestion successful")
        return 0
    except Exception as e:
        logging.error("Data ingestion failed: %s", e)
        return 1

if __name__ == "__main__":
    api_url = 'https://api.example.com/data'
    status = fetch_data(api_url, 'data/raw_data.json')
    exit(status)
