import requests
import pandas as pd
from datetime import datetime
import os

def fetch_api_data(api_url):
    """Récupère les données depuis une API."""
    response = requests.get(api_url)
    response.raise_for_status()  # Lève une exception si la requête échoue
    data = response.json()
    return pd.DataFrame(data)  # Convertit les données en DataFrame

def save_raw_data(df, output_file):
    """Sauvegarde les données brutes dans un fichier CSV."""
    # Vérifiez si le répertoire existe, sinon créez-le
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Répertoire créé : {output_dir}")
    
    # Sauvegarde des données
    df.to_csv(output_file, index=False)
    print(f"Données brutes sauvegardées dans {output_file}")

if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com/posts"  # Exemple d'API factice
    df = fetch_api_data(API_URL)
    save_raw_data(df, f"../data/raw/raw_data_{datetime.now().strftime('%Y-%m-%d')}.csv")
