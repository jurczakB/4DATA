import requests
import json
import logging

def fetch_data(api_url, output_path):
    try:
        logging.info(f"Fetching data from API: {api_url}")
        response = requests.get(api_url)
        if response.status_code == 200:
            with open(output_path, 'w') as f:
                json.dump(response.json(), f)
            logging.info(f"Data successfully saved to {output_path}")
            return True
        else:
            logging.error(f"Failed to fetch data. Status Code: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f"Error occurred while fetching data: {e}")
        return False