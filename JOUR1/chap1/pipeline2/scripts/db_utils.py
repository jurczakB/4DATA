import pandas as pd
import sqlite3

def load_to_db(input_file, db_file, table_name):
    """Charge les données dans une base SQLite."""
    conn = sqlite3.connect(db_file)
    data = pd.read_csv(input_file)
    data.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()
    print(f"Données chargées dans la table {table_name} de {db_file}")

if __name__ == "__main__":
    load_to_db("../data/processed/transformed_data.csv", "../data/data_pipeline.db", "daily_data")
