# TP : Introduction à Python et ses bibliothèques pour la manipulation de données

## Objectif

Ce TP a pour but de vous familiariser avec **Python** et les bibliothèques fondamentales utilisées dans les pipelines de données. Vous apprendrez à manipuler des fichiers CSV et JSON, à utiliser **NumPy** et **Pandas** pour le traitement des données tabulaires et à interagir avec **SQLite** via SQLAlchemy.

Nous allons structurer le projet selon une arborescence bien définie pour organiser les fichiers et scripts.

## Arborescence du projet

Voici l'arborescence recommandée :

```bash
python-data-pipeline/
├── data/
│   ├── input/
│   │   ├── sample.csv
│   │   ├── sample.json
│   ├── output/
│   │   ├── filtered_data.csv
│   │   ├── transformed.json
├── scripts/
│   ├── load_csv.py
│   ├── manipulate_json.py
│   ├── pandas_analysis.py
│   ├── sqlite_interaction.py
│   ├── scheduler.py
├── requirements.txt
├── README.md
```

---

## 1. Installation et configuration de l'environnement

Avant de commencer, assurez-vous que **Python 3.8+** est installé sur votre machine. 

### Installation de l'environnement virtuel

```sh
# Création d'un environnement virtuel
python3 -m venv venv

# Activation (Windows)
venv\Scripts\activate

# Activation (Mac/Linux)
source venv/bin/activate
```

### Installation des bibliothèques nécessaires

```sh
pip install numpy pandas matplotlib seaborn jupyter notebook sqlalchemy sqlite3
```

Ajoutez ces dépendances dans `requirements.txt` pour garder une trace des packages installés :

```sh
pip freeze > requirements.txt
```
---

## 2. Bases de Python 

### 2.1. Structures de données

#### Listes
```python
fruits = ["pomme", "banane", "cerise"]
fruits.append("orange")
print(fruits[0])  # pomme
```

#### Dictionnaires
```python
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(personne["nom"])  # Alice
personne["age"] = 26  # Modification
```

#### Boucles et conditions
```python
for fruit in fruits:
    print(fruit)

if "pomme" in fruits:
    print("Il y a une pomme !")
```

#### Fonctions
```python
def carre(x):
    return x * x

print(carre(4))  # 16
```

---

## 3. Manipulation de fichiers CSV et JSON

### 3.1. Lecture et écriture de fichiers CSV

```python
import csv

# Lecture CSV
with open("data/input/data.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

```python
# Écriture CSV
with open("data/output/output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nom", "Age"])
    writer.writerow(["Alice", 25])
```

### 3.2. Manipulation de JSON

```python
import json

# Lecture JSON
with open("data/input/data.json", "r") as file:
    data = json.load(file)
    print(data)

# Écriture JSON
data = {"nom": "Alice", "age": 25}
with open("data/output/output.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

## 4. Manipulation des données avec Pandas

### 4.1. Chargement et affichage des données

```python
import pandas as pd

# Charger un CSV
df = pd.read_csv("data/input/data.csv")
print(df.head())
```

### 4.2. Sélection et filtrage

```python
# Sélection d'une colonne
print(df["Nom"])

# Filtrage
df_filtre = df[df["Age"] > 25]
print(df_filtre)
```

### 4.3. Manipulation et transformations

```python
# Ajouter une colonne
df["Année de naissance"] = 2023 - df["Age"]
```

```python
# Supprimer une colonne
df.drop(columns=["Adresse"], inplace=True)
```

### 4.4. Agrégation et statistiques

```python
# Statistiques
df.describe()

# Grouper par ville
print(df.groupby("Ville")["Age"].mean())
```

---

## 5. NumPy pour les calculs numériques

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)
print(np.mean(arr))
```

---

## 6. Introduction à SQLite et SQLAlchemy

### 6.1. Connexion à SQLite

```python
from sqlalchemy import create_engine
engine = create_engine("sqlite:///data/database.db")
connection = engine.connect()
```

### 6.2. Création d'une table et insertion de données

```python
connection.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
connection.execute("""
INSERT INTO users (name, age) VALUES ('Alice', 25), ('Bob', 30)
""")
```

### 6.3. Lecture avec Pandas

```python
df = pd.read_sql("SELECT * FROM users", con=engine)
print(df)
```

---

## Exercices

1. **Créer un script Python** qui charge un CSV, filtre les lignes et enregistre le résultat.
2. **Manipuler JSON** : lire et écrire un fichier JSON.
3. **Utiliser Pandas** pour grouper et analyser un dataset.
4. **Interagir avec SQLite** via SQLAlchemy.

---

---

## Etape 0: Analyse exploratoire des données

Avant de commencer à manipuler les données avec Python et Pandas, il est essentiel de comprendre leur structure et leur contenu. Cette première étape consiste à charger les datasets et effectuer une analyse exploratoire.

### Objectifs :
- Charger les fichiers de données (`sales_data.csv`, `customers.csv`, `orders.json`)
- Vérifier la structure des datasets (types de colonnes, valeurs manquantes, doublons, etc.)
- Analyser les statistiques descriptives
- Visualiser les distributions et les relations entre variables

### 1. Charger les fichiers de données

Utiliser Pandas pour charger les fichiers et afficher les premières lignes :

```python
import pandas as pd

# Charger les fichiers CSV
df_sales = pd.read_csv("data/sales_data.csv")
df_customers = pd.read_csv("data/customers.csv")

# Charger le fichier JSON
df_orders = pd.read_json("data/orders.json")

# Aperçu des données
print(df_sales.head())
print(df_customers.head())
print(df_orders.head())
```

### 2. Vérifier la structure des données

Afficher les types de colonnes et identifier les valeurs manquantes :

```python
# Vérifier la structure des datasets
print(df_sales.info())
print(df_customers.info())
print(df_orders.info())

# Vérifier les valeurs manquantes
print(df_sales.isnull().sum())
print(df_customers.isnull().sum())
print(df_orders.isnull().sum())
```

### 3. Analyser les statistiques descriptives

Obtenir des résumés statistiques pour les colonnes numériques :

```python
# Statistiques descriptives
df_sales.describe()
df_customers.describe()
df_orders.describe()
```

### 4. Visualiser les données

Créer des graphiques pour explorer les distributions et les relations entre variables :

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Histogramme des montants de ventes
plt.figure(figsize=(10, 5))
sns.histplot(df_sales["total_amount"], bins=30, kde=True)
plt.title("Distribution des montants de ventes")
plt.show()

# Répartition des commandes par pays
plt.figure(figsize=(12, 5))
df_customers["country"].value_counts().plot(kind="bar")
plt.title("Nombre de clients par pays")
plt.xticks(rotation=45)
plt.show()
```
---

Cette première partie est essentielle pour comprendre les bases avant d'aborder la **construction de pipelines de données** dans la suite du TP.

## 1. Chargement et manipulation de fichiers CSV

### Objectif :
Charger un fichier CSV, appliquer des filtres et sauvegarder un nouveau fichier transformé.

### Fichier : `scripts/load_csv.py`

### Exercices pratiques :

1. **Charger un fichier CSV en DataFrame avec Pandas.**
   ```python
   import pandas as pd
   df = pd.read_csv("data/sales_data.csv")
   print(df.head())
   ```

2. **Filtrer les lignes selon une condition donnée (ex: garder uniquement les valeurs supérieures à 500 dans une colonne `total_amount`).**
   ```python
   df_filtered = df[df['total_amount'] > 500]
   print(df_filtered.head())
   ```

3. **Remplacer les valeurs manquantes d’une colonne par la moyenne des valeurs existantes.**
   ```python
   df['total_amount'].fillna(df['total_amount'].mean(), inplace=True)
   ```

4. **Renommer certaines colonnes du fichier CSV.**
   ```python
   df.rename(columns={'old_column': 'new_column'}, inplace=True)
   ```

5. **Trier le DataFrame par plusieurs colonnes.**
   ```python
   df_sorted = df.sort_values(by=['customer_id', 'total_amount'], ascending=[True, False])
   ```

6. **Sauvegarder le DataFrame filtré dans un fichier `filtered_data.csv`.**
   ```python
   df_filtered.to_csv("data/output/filtered_data.csv", index=False)
   ```

---

## 2. Lecture et manipulation de fichiers JSON

### Objectif :
Lire un fichier JSON, modifier son contenu, et sauvegarder un fichier transformé.

### Fichier : `scripts/manipulate_json.py`

### Exercices pratiques :

1. **Charger un fichier JSON en Python.**
   ```python
   import json
   with open("data/customers.json") as f:
       data = json.load(f)
   ```

2. **Modifier une clé spécifique d’un dictionnaire JSON.**
   ```python
   data["customer_name"] = "John Doe"
   ```

3. **Ajouter un nouvel élément à un fichier JSON.**
   ```python
   data["new_key"] = "new_value"
   ```

4. **Supprimer une clé spécifique du fichier JSON.**
   ```python
   del data["old_key"]
   ```

5. **Convertir un fichier JSON en DataFrame Pandas.**
   ```python
   import pandas as pd
   df = pd.DataFrame.from_dict(data)
   ```

6. **Sauvegarder les modifications dans un fichier `transformed.json`.**
   ```python
   with open("data/output/transformed.json", "w") as f:
       json.dump(data, f, indent=4)
   ```

---

## 3. Analyse de données avec Pandas

### Objectif :
Charger un dataset et réaliser des statistiques descriptives.

### Fichier : `scripts/pandas_analysis.py`

### Exercices pratiques :

1. **Charger un dataset et afficher ses informations générales.**
   ```python
   df.info()
   df.describe()
   ```

2. **Grouper les données par une colonne et calculer la moyenne d’une autre colonne.**
   ```python
   df_grouped = df.groupby('customer_id')['total_amount'].mean()
   ```

3. **Filtrer un DataFrame pour afficher uniquement certaines valeurs.**
   ```python
   df_filtered = df[df['country'] == 'France']
   ```

4. **Fusionner deux DataFrames en utilisant une clé commune.**
   ```python
   df_merged = pd.merge(df_customers, df_sales, on='customer_id')
   ```

5. **Créer une nouvelle colonne calculée à partir d’autres colonnes.**
   ```python
   df['total_with_tax'] = df['total_amount'] * 1.2
   ```

6. **Générer un histogramme d’une colonne spécifique.**
   ```python
   import matplotlib.pyplot as plt
   df['total_amount'].hist()
   plt.show()
   ```

---

## 4. Interagir avec SQLite via SQLAlchemy

### Objectif :
Créer une base de données SQLite, insérer des données et les manipuler avec SQLAlchemy.

### Fichier : `scripts/sqlite_interaction.py`

### Exercices pratiques :

1. **Créer une base de données SQLite et une table avec SQLAlchemy.**
   ```python
   from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
   engine = create_engine("sqlite:///data/database.db")
   metadata = MetaData()
   customers = Table('customers', metadata,
       Column('id', Integer, primary_key=True),
       Column('name', String),
       Column('total_spent', Float)
   )
   metadata.create_all(engine)
   ```

2. **Insérer plusieurs lignes de données dans une table.**
   ```python
   from sqlalchemy.orm import sessionmaker
   Session = sessionmaker(bind=engine)
   session = Session()
   session.execute(customers.insert().values(id=1, name="Alice", total_spent=200.0))
   session.commit()
   ```

3. **Exécuter une requête SELECT pour récupérer toutes les données d’une table.**
   ```python
   result = session.execute(customers.select()).fetchall()
   for row in result:
       print(row)
   ```

4. **Filtrer les résultats d’une requête SQLAlchemy.**
   ```python
   result = session.execute(customers.select().where(customers.c.total_spent > 100)).fetchall()
   ```

5. **Mettre à jour une entrée spécifique dans la base de données.**
   ```python
   session.execute(customers.update().where(customers.c.id == 1).values(total_spent=300.0))
   session.commit()
   ```

6. **Convertir le résultat d’une requête SQL en DataFrame Pandas.**
   ```python
   import pandas as pd
   df = pd.read_sql("SELECT * FROM customers", engine)
   ```

   ---

## 3. Création de pipelines de données (ETL)

### Objectif :
Créer une première pipeline ETL permettant d’extraire, transformer et charger des données en automatisant les tâches. Ci-après figurent des indications et des pistes avec des extraits de code. Cependant, c'est à vous de bien stucturer les étapes de cette première pipeline en utilisant les bonnes pratiques vues durant le cours (fonctions réutilisables, logs, documentation des fonctions, utiliser les bons scripts python pour la bonne action,...)

### Structure du pipeline :
Le pipeline sera structuré en trois étapes principales :
1. **Extraction** : Charger des fichiers CSV et JSON en DataFrame.
2. **Transformation** : Nettoyage et enrichissement des données.
3. **Chargement** : Sauvegarde des données dans une base SQLite.

### Fichier : `scripts/etl_pipeline.py`

### Étapes de la pipeline :

#### 1. Extraction des données

```python
import pandas as pd
import json

def extract_csv(file_path):
    return pd.read_csv(file_path)

def extract_json(file_path):
    with open(file_path, "r") as f:
        return pd.DataFrame(json.load(f))

sales_data = extract_csv("data/sales_data.csv")
customers_data = extract_json("data/customers.json")
```

#### 2. Transformation des données

```python
# Nettoyage des données
sales_data.dropna(inplace=True)
sales_data = sales_data[sales_data['total_amount'] > 0]

# Fusion avec les données clients
merged_data = pd.merge(sales_data, customers_data, on='customer_id', how='left')

# Création d’une nouvelle colonne
merged_data['total_with_tax'] = merged_data['total_amount'] * 1.2
```

#### 3. Chargement des données dans SQLite

```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/database.db")
merged_data.to_sql("sales_data", con=engine, if_exists="replace", index=False)
```

#### 4. Planification de l'exécution (Scheduling)

Un pipeline ETL peut être automatisé à l'aide de `cron` sous Linux ou d'un planificateur de tâches sous Windows.

**Exemple de configuration avec `cron` :**

Ouvrir le crontab avec la commande :
```bash
crontab -e
```

Ajouter une ligne pour exécuter le script tous les jours à minuit :
```bash
0 0 * * * /usr/bin/python3 /chemin/vers/le_projet/scripts/etl_pipeline.py
```

**Sur Windows, utiliser le planificateur de tâches :**
- Créer une nouvelle tâche
- Sélectionner "Exécuter un programme"
- Ajouter `python.exe` comme programme et `C:\chemin\vers\le_projet\scripts\etl_pipeline.py` comme argument.

---

### Conclusion
Cette première pipeline de données permet d’acquérir les bases de la manipulation et de l’automatisation des traitements de données. Elle sera la base des prochaines étapes, où nous intégrerons des outils avancés comme **Apache Airflow** ou **Dagster** pour orchestrer et surveiller les pipelines de données de manière plus robuste.

📌 **Prochaine étape :** Améliorer la pipeline en ajoutant des logs et la gestion des erreurs pour rendre l’automatisation plus fiable.

