import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connexion à la base de données SQLite
db_path = "sales_data.db"
conn = sqlite3.connect(db_path)

# Chargement des données de la table 'sales'
query = "SELECT COUNTRY, PRODUCTLINE, SALES, QUANTITYORDERED FROM sales"
sales_data = pd.read_sql_query(query, conn)

# Fermeture de la connexion
conn.close()

# Aperçu des données
print(sales_data.head())

# Configuration de style pour les visualisations
sns.set_theme(style="whitegrid")

# Graphique 1 : Ventes totales par pays
plt.figure(figsize=(12, 6))
country_sales = sales_data.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)
sns.barplot(x=country_sales.index, y=country_sales.values, palette="viridis")
plt.title("Ventes totales par pays", fontsize=16)
plt.xlabel("Pays", fontsize=12)
plt.ylabel("Ventes totales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./data/plots/country_sales.png")  # Sauvegarder le graphique
plt.show()

# Graphique 2 : Ventes par ligne de produit
plt.figure(figsize=(12, 6))
productline_sales = sales_data.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)
sns.barplot(x=productline_sales.index, y=productline_sales.values, palette="rocket")
plt.title("Ventes par ligne de produit", fontsize=16)
plt.xlabel("Ligne de produit", fontsize=12)
plt.ylabel("Ventes totales ($)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("./data/plots/productline_sales.png")  # Sauvegarder le graphique
plt.show()

# Graphique 3 : Quantités commandées par pays et produit (carte thermique)
plt.figure(figsize=(12, 8))
heatmap_data = sales_data.pivot_table(values="QUANTITYORDERED", index="COUNTRY", columns="PRODUCTLINE", aggfunc="sum")
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="coolwarm", linewidths=.5)
plt.title("Quantités commandées par pays et produit", fontsize=16)
plt.xlabel("Ligne de produit", fontsize=12)
plt.ylabel("Pays", fontsize=12)
plt.tight_layout()
plt.savefig("./data/plots/heatmap_quantities.png")  # Sauvegarder le graphique
plt.show()
