import pandas as pd
import logging

def clean_data(input_path, output_path):
    try:
        logging.info(f"Reading data from {input_path}")
        df = pd.read_json(input_path)
        # df = df.dropna()
        df['price'] = df['current_price'].astype(float)
        df['market_cap'] = df['market_cap'].astype(float)
        df['price_change_percentage_24h'] = df['price_change_percentage_24h'].fillna(0)
        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}")
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")