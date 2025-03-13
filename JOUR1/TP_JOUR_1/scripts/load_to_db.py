import pandas as pd
import psycopg2
import logging

def load_data_to_db(csv_path, db_config):
    conn = None
    cursor = None
    try:
        logging.info("Connecting to PostgreSQL database")
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS crypto_data (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                current_price FLOAT,
                market_cap FLOAT,
                price_change_percentage_24h FLOAT
            )
        """)
        conn.commit()
        logging.info("Table 'crypto_data' is ready")

        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO crypto_data (name, current_price, market_cap, price_change_percentage_24h)
                VALUES (%s, %s, %s, %s)
            """, (row['name'], row['current_price'], row['market_cap'], row['price_change_percentage_24h']))

        conn.commit()
        logging.info(f"Data from {csv_path} successfully loaded into PostgreSQL")

    except Exception as e:
        logging.error(f"Error while loading data to PostgreSQL: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()