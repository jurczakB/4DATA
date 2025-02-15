import pandas as pd
from sqlalchemy import create_engine
import logging

# Configuration du logging
logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extract(file_path):
    """Extraction des données du fichier CSV."""
    logging.info("Début de l'étape d'extraction")
    sales_data = pd.read_csv(file_path, encoding='Windows-1252')
    logging.info(f"Extraction terminée, {len(sales_data)} lignes chargées.")
    return sales_data

def transform(sales_data):
    """Nettoyage et agrégation des données."""
    logging.info("Début de l'étape de transformation")
    # Convertir les dates au format standard
    sales_data['ORDERDATE'] = pd.to_datetime(sales_data['ORDERDATE'], errors='coerce')
    
    # Supprimer les lignes avec des dates invalides
    sales_data = sales_data.dropna(subset=['ORDERDATE'])
    
    # Agréger les ventes par pays et ligne de produit
    aggregated_data = sales_data.groupby(['COUNTRY', 'PRODUCTLINE']).agg({
        'SALES': 'sum',
        'QUANTITYORDERED': 'sum'
    }).reset_index()
    
    logging.info(f"Transformation terminée, {len(aggregated_data)} lignes agrégées.")
    return aggregated_data

def load(aggregated_data, db_path):
    """Chargement des données dans la base SQLite."""
    logging.info("Début de l'étape de chargement")
    engine = create_engine(f'sqlite:///{db_path}')
    aggregated_data.to_sql('sales', engine, if_exists='replace', index=False)
    logging.info("Chargement terminé avec succès dans la base SQLite.")

def main():
    """Pipeline complet ETL."""
    logging.info("Démarrage du pipeline ETL")
    file_path = "./data/sales/sales_data_sample.csv"  # Chemin du fichier CSV
    db_path = "sales_data.db"

    # Étape 1 : Extraction
    sales_data = extract(file_path)

    # Étape 2 : Transformation
    aggregated_data = transform(sales_data)

    # Étape 3 : Chargement
    load(aggregated_data, db_path)
    
    logging.info("Pipeline ETL exécuté avec succès")

if __name__ == "__main__":
    main()