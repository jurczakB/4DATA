# 🔥 TP : Pipelines de Données avec Python et SQL 🔥

## 📌 Objectif

L'objectif de ce TP est de vous **familiariser avec les outils et langages clés** pour manipuler et transformer des données. Vous allez explorer :
- **Python** et ses bibliothèques : `pandas`, `numpy`, `sqlalchemy`, `matplotlib`...
- **SQL** et les bases de données avec **SQLite**.
- **Les bases des pipelines de données** : ingestion, transformation et stockage.

À travers ce TP, vous construirez **vos premiers pipelines de données sans orchestrateur**.

---

## 🚀 Partie 1 : Manipulation des données avec Python  

### 1️⃣ Lecture et manipulation de fichiers CSV

📂 Un fichier `data.csv` contient les colonnes suivantes :

```
ID,Nom,Age,Score
1,Alice,25,90
2,Bob,30,80
3,Charlie,22,95
```

✅ **À faire :**
- **1.1** Lire le fichier CSV et afficher son contenu ligne par ligne.
- **1.2** Charger le fichier dans un **DataFrame Pandas** et afficher les **3 premières lignes**.

---

### 2️⃣ Nettoyage et transformation des données

✅ **À faire :**
- **2.1** Vérifier la présence de **valeurs manquantes** et les traiter (remplacement ou suppression).
- **2.2** Filtrer les étudiants ayant un score **supérieur à 85**.
- **2.3** Ajouter une colonne `Categorie` :
  - `Excellent` pour un **score ≥ 90**.
  - `Bon` pour un **score entre 80 et 89**.
  - `Moyen` pour un **score < 80**.

---

### 3️⃣ Calculs statistiques et visualisation

✅ **À faire :**
- **3.1** Calculer la **moyenne**, le **score minimum** et le **score maximum** des étudiants.
- **3.2** Générer un **histogramme** de la répartition des âges (`matplotlib`).
- **3.3** Sauvegarder le **DataFrame nettoyé** en **CSV (`data_cleaned.csv`)**.

---

## 🐴 Partie 2 : Stockage et interrogation des données avec SQLite  

### 4️⃣ Création d’une base de données SQLite

✅ **À faire :**
- **4.1** Créer une **base de données SQLite** (`database.db`).
- **4.2** Créer une **table Étudiants** avec les colonnes suivantes :
  - `id` (clé primaire)
  - `nom` (texte)
  - `age` (entier)
  - `score` (réel)
  - `categorie` (texte)

---

### 5️⃣ Insertion et interrogation des données

✅ **À faire :**
- **5.1** Insérer les données du **fichier `data_cleaned.csv`** dans la base de données.
- **5.2** Afficher tous les étudiants ayant un **âge > 25 ans**.
- **5.3** Calculer le **score moyen par catégorie**.

---

## 🔄 Partie 3 : Construction d’un pipeline de données

🎯 **Objectif :** Automatiser l’ensemble du pipeline.

✅ **À faire :**
- **6.1** Écrire un **script Python complet** exécutant :
  1. Chargement des données.
  2. Nettoyage et transformation.
  3. Stockage dans **SQLite**.
  4. Génération d’un **rapport CSV et d’une visualisation**.

**Bonus :** Ajouter une fonction permettant **des requêtes SQL dynamiques**.

---

## ✅ Validation et rendu

📥 **À rendre :**
- Un **script Python final (`pipeline.py`)**.
- La **base de données SQLite (`database.db`)**.
- Un **fichier CSV nettoyé (`data_cleaned.csv`)**.
- Une **explication rapide** du pipeline.

---

## 🎯 Compétences acquises

✅ **Manipulation avancée avec Pandas**  
✅ **Nettoyage et transformation des données**  
✅ **Stockage et interrogation en SQL (SQLite)**  
✅ **Visualisation avec Matplotlib**  
✅ **Automatisation d’un pipeline de données**  

Bonne pratique et bon courage ! 🚀💡
