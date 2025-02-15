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
python -m venv venv

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

Cette première partie est essentielle pour comprendre les bases avant d'aborder la **construction de pipelines de données** dans la suite du TP.

### 1. Chargement et manipulation de fichiers CSV

📌 **Objectif** : Charger un fichier CSV, appliquer des filtres et sauvegarder un nouveau fichier transformé.

📍 **Fichier :** `scripts/load_csv.py`

💡 **Exercices pratiques :**

1. Charger un fichier CSV en DataFrame avec Pandas.
   - Utiliser `pd.read_csv("data/input/sample.csv")`
   - Afficher les 5 premières lignes.

2. Filtrer les lignes selon une condition donnée (ex: garder uniquement les valeurs supérieures à 50 dans une colonne donnée).
   - Utiliser `df[df['colonne'] > 50]`

3. Remplacer les valeurs manquantes d’une colonne par la moyenne des valeurs existantes.
   - Utiliser `df['colonne'].fillna(df['colonne'].mean())`

4. Renommer certaines colonnes du fichier CSV.
   - Utiliser `df.rename(columns={'ancienne_colonne': 'nouvelle_colonne'})`

5. Trier le DataFrame par plusieurs colonnes.
   - Utiliser `df.sort_values(by=['colonne1', 'colonne2'], ascending=[True, False])`

6. Sauvegarder le DataFrame filtré dans un fichier `filtered_data.csv`.
   - Utiliser `df.to_csv("data/output/filtered_data.csv", index=False)`

---

### 2. Lecture et manipulation de fichiers JSON

📌 **Objectif** : Lire un fichier JSON, modifier son contenu, et sauvegarder un fichier transformé.

📍 **Fichier :** `scripts/manipulate_json.py`

💡 **Exercices pratiques :**

1. Charger un fichier JSON en Python.
   - Utiliser `json.load(open("data/input/sample.json"))`

2. Modifier une clé spécifique d’un dictionnaire JSON.
   - Ex: `data["clé"] = "nouvelle_valeur"`

3. Ajouter un nouvel élément à un fichier JSON.
   - Ex: `data["nouvelle_clé"] = "valeur"`

4. Supprimer une clé spécifique du fichier JSON.
   - Utiliser `del data["clé"]`

5. Convertir un fichier JSON en DataFrame Pandas.
   - Utiliser `pd.DataFrame.from_dict(data)`

6. Sauvegarder les modifications dans un fichier `transformed.json`.
   - Utiliser `json.dump(data, open("data/output/transformed.json", "w"))`

---

### 3. Analyse de données avec Pandas

📌 **Objectif** : Charger un dataset et réaliser des statistiques descriptives.

📍 **Fichier :** `scripts/pandas_analysis.py`

💡 **Exercices pratiques :**

1. Charger un dataset et afficher ses informations générales.
   - `df.info()` et `df.describe()`

2. Grouper les données par une colonne spécifique et calculer la moyenne d’une autre colonne.
   - `df.groupby('colonne_groupe')['colonne_cible'].mean()`

3. Filtrer un DataFrame pour afficher uniquement certaines valeurs.
   - `df[df['colonne'] == 'valeur spécifique']`

4. Fusionner deux DataFrames en utilisant une clé commune.
   - `pd.merge(df1, df2, on='colonne_commune')`

5. Créer une nouvelle colonne calculée à partir d’autres colonnes.
   - `df['nouvelle_colonne'] = df['col1'] + df['col2']`

6. Générer un histogramme d’une colonne spécifique.
   - `df['colonne'].hist()`

---

### 4. Interagir avec SQLite via SQLAlchemy

📌 **Objectif** : Créer une base de données SQLite, insérer des données et les manipuler avec SQLAlchemy.

📍 **Fichier :** `scripts/sqlite_interaction.py`

💡 **Exercices pratiques :**

1. Créer une base de données SQLite et une table avec SQLAlchemy.
   - `engine = create_engine("sqlite:///data/database.db")`
   - `Base.metadata.create_all(engine)`

2. Insérer plusieurs lignes de données dans une table.
   - `session.add_all([Objet1, Objet2])`

3. Exécuter une requête SELECT pour récupérer toutes les données d’une table.
   - `session.query(Objet).all()`

4. Filtrer les résultats d’une requête SQLAlchemy.
   - `session.query(Objet).filter(Objet.colonne == valeur).all()`

5. Mettre à jour une entrée spécifique dans la base de données.
   - `session.query(Objet).filter(Objet.id == valeur).update({Objet.colonne: nouvelle_valeur})`

6. Convertir le résultat d’une requête SQL en DataFrame Pandas.
   - `pd.read_sql("SELECT * FROM table", engine)`
