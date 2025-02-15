import pandas as pd

def transform_data(input_file, output_file):
    """Nettoie et transforme les données brutes."""
    data = pd.read_csv(input_file)
    # Transformation exemple : Ajout d'une colonne 'processed_date'
    data['processed_date'] = pd.Timestamp.now()
    data.to_csv(output_file, index=False)
    print(f"Données transformées sauvegardées dans {output_file}")

if __name__ == "__main__":
    transform_data("../data/raw/raw_data.csv", "../data/processed/transformed_data.csv")
