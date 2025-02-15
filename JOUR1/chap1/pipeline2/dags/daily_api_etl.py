from dagster import job, op
from scripts.fetch_data import fetch_api_data, save_raw_data
from scripts.transform_data import transform_data
from scripts.db_utils import load_to_db
from datetime import datetime

API_URL = "https://jsonplaceholder.typicode.com/posts"
RAW_DATA_FILE = f"../data/raw/raw_data_{datetime.now().strftime('%Y-%m-%d')}.csv"
TRANSFORMED_DATA_FILE = "../data/processed/transformed_data.csv"
DB_FILE = "../data/data_pipeline.db"

@op
def fetch_data_op():
    """Tâche pour récupérer les données."""
    df = fetch_api_data(API_URL)
    save_raw_data(df, RAW_DATA_FILE)

@op
def transform_data_op():
    """Tâche pour transformer les données."""
    transform_data(RAW_DATA_FILE, TRANSFORMED_DATA_FILE)

@op
def load_data_op():
    """Tâche pour charger les données dans la base."""
    load_to_db(TRANSFORMED_DATA_FILE, DB_FILE, "daily_data")

@job
def daily_pipeline():
    """Pipeline Dagster quotidien."""
    raw_data = fetch_data_op()
    transformed_data = transform_data_op()
    load_data_op()
