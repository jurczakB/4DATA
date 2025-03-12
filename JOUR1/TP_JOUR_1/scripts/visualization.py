import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import logging
import os
from dotenv import load_dotenv
import numpy as np

load_dotenv()

def visualize_data(db_path, output_path):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM crypto_data", conn)
    conn.close()

    logging.info(f"DataFrame columns: {df.columns}")
    logging.info(f"DataFrame dtypes: {df.dtypes}")
    logging.info(f"First few rows of data:\n{df.head()}")

    plt.figure(figsize=(12, 8))
    # Visualisation des 10 cryptos avec la plus grande capitalisation boursière
    top_10 = df.nlargest(10, 'market_cap')
    plt.barh(top_10['name'], top_10['market_cap'])
    plt.xlabel('Market Cap (USD)')
    plt.ylabel('Cryptocurrency')
    plt.title('Top 10 Cryptocurrencies by Market Capitalization')
    plt.tight_layout()
    plt.savefig(output_path)
    logging.info(f"Visualization saved to {output_path}")
