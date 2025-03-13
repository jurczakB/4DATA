from extract_api import fetch_data
from transform_data import clean_data
from load_to_db import load_data_to_db
from visualization import visualize_data
import os
from dotenv import load_dotenv
import logging

load_dotenv()

def run_etl():
    log_file = os.getenv('LOG_FILE')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    api_url = os.getenv('API_URL')
    raw_data_path = os.getenv('RAW_DATA_PATH')
    clean_data_path = os.getenv('CLEAN_DATA_PATH')
    visual_output_path = os.getenv('VISUAL_OUTPUT_PATH')

    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }

    logging.info("Starting ETL process...")

    if fetch_data(api_url, raw_data_path):
        logging.info("Data extraction successful.")
        clean_data(raw_data_path, clean_data_path)
        logging.info("Data transformation successful.")
        load_data_to_db(clean_data_path, db_config)
        logging.info("Data loading to PostgreSQL successful.")
        visualize_data(db_config, visual_output_path)
        logging.info("Visualization generated successfully.")
    else:
        logging.error("Data extraction failed.")

if __name__ == "__main__":
    run_etl()
