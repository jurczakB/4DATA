import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import logging

def visualize_data(db_config, output_path):
    try:
        logging.info("Generating visualization from PostgreSQL data")
        db_url = f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
        engine = create_engine(db_url)

        df = pd.read_sql("SELECT name, market_cap FROM crypto_data ORDER BY market_cap DESC LIMIT 10", engine)

        plt.figure(figsize=(12, 8))
        plt.barh(df['name'], df['market_cap'])
        plt.xlabel('Market Cap (USD)')
        plt.ylabel('Cryptocurrency')
        plt.title('Top 10 Cryptocurrencies by Market Capitalization')
        plt.tight_layout()
        plt.savefig(output_path)
        logging.info(f"Visualization saved to {output_path}")

    except Exception as e:
        logging.error(f"Error while generating visualization: {e}")