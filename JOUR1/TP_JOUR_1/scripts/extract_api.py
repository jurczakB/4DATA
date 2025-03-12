import requests
import json
import logging

def fetch_data(api_url, output_path):
    response = requests.get(api_url)
    if response.status_code == 200:
        with open(output_path, 'w') as f:
            json.dump(response.json(), f)
        logging.info(f"Data saved to {output_path}")
    else:
        logging.error(f"Failed to fetch data: {response.status_code}")