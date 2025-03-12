import sqlite3
import pandas as pd
import logging

def load_data_to_db(csv_path, db_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_csv(csv_path)
    df.to_sql('crypto_data', conn, if_exists='replace', index=False)
    conn.close()
    logging.info(f"Data loaded to database at {db_path}")