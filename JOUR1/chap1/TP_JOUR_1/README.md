# TP : Introduction à Python et ses bibliothèques pour la manipulation de données

## Objectif

Ce TP a pour but de vous familiariser avec **Python** et les bibliothèques fondamentales utilisées dans les pipelines de données. Vous apprendrez à manipuler des fichiers CSV et JSON, à utiliser **NumPy** et **Pandas** pour le traitement des données tabulaires et à interagir avec **SQLite** via SQLAlchemy.

Nous allons structurer le projet selon une arborescence bien définie pour organiser les fichiers et scripts.

## Arborescence du projet

Voici l'arborescence recommandée :

```
projet_pipeline/
│-- data/                  # Dossiers contenant les fichiers de données
│   ├── input/             # Fichiers bruts (CSV, JSON, etc.)
│   ├── processed/         # Fichiers traités et nettoyés
│   ├── output/            # Résultats finaux
│
│-- notebooks/             # Notebooks Jupyter pour l'exploration des données
│
│-- scripts/               # Scripts Python
│   ├── data_cleaning.py   # Nettoyage des données
│   ├── data_analysis.py   # Analyse et statistiques
│   ├── database.py        # Interaction avec SQLite
│
│-- requirements.txt       # Liste des dépendances
│-- README.md              # Ce fichier
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
