from extract_api import fetch_data
from transform_data import clean_data
from load_data_to_db import load_data_to_db
from visualization import visualize_data
import logging
import os
from dotenv import load_dotenv

load_dotenv()

def run_etl():
    log_file = os.getenv('LOG_FILE')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    api_url = os.getenv('API_URL')
    raw_data_path = os.getenv('RAW_DATA_PATH')
    clean_data_path = os.getenv('CLEAN_DATA_PATH')
    db_path = os.getenv('DB_PATH')
    visual_output_path = os.getenv('VISUAL_OUTPUT_PATH')

    logging.info("Starting ETL process...")
    fetch_data(api_url, raw_data_path)
    clean_data(raw_data_path, clean_data_path)
    load_data_to_db(clean_data_path, db_path)
    visualize_data(db_path, visual_output_path)
    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    run_etl()