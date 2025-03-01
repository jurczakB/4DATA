# Travail Pratique (TP) : Prise en main de DBT en local

## 📌 Contexte et objectif

Vous êtes **Data Engineer** dans une entreprise de e-commerce. La direction souhaite avoir une **meilleure visibilité sur les ventes, les clients et les produits** pour optimiser les décisions stratégiques. Cependant, les données sont actuellement stockées sous forme de **fichiers CSV** dispersés et difficiles à exploiter.

Votre mission : **structurer et transformer ces données en créant un modèle analytique exploitable avec DBT**, le tout **en local, sans connexion à un Data Warehouse externe**.

---

## 📂 Données fournies
Vous disposez de plusieurs fichiers CSV situés dans le dossier `data/` :
- `orders.csv` : Contient les commandes passées sur le site e-commerce
- `customers.csv` : Contient les informations des clients
- `products.csv` : Liste des produits disponibles

### **📥 Télécharger les données**
Les fichiers de données sont fournis dans ce dépôt, sous `data/`. Vous pouvez les **inspecter avant de commencer**.

---

## 📝 Partie 1 - Installation et configuration de DBT
### 📍 Objectif : Installer DBT et configurer un projet en local

### 🔹 Étape 1 : Installation de DBT
1. **Installer DBT** avec Python :
   ```sh
   pip install dbt-core dbt-duckdb
   ```
2. **Vérifier l’installation** :
   ```sh
   dbt --version
   ```

### 🔹 Étape 2 : Configuration du projet DBT
1. **Créez un nouveau projet DBT.**
2. **Modifiez le fichier `profiles.yml`** pour configurer DBT afin qu’il fonctionne avec DuckDB et stocke les données localement.
3. **Testez la connexion locale** pour vous assurer que tout fonctionne correctement.

💡 **Indice** : DBT doit être configuré avec un type de connexion **DuckDB** et un chemin de stockage local pour la base de données.

<details>
  <summary>Afficher le code</summary>

  ```sh
  dbt init tp_dbt
  cd tp_dbt

</details> ```

1. **Créer un nouveau projet DBT** :
   ```sh
   dbt init tp_dbt
   cd tp_dbt
   ```
2. **Configurer DBT pour fonctionner en local avec DuckDB** (un moteur SQL léger basé sur des fichiers) :
   Modifier le fichier `~/.dbt/profiles.yml` :
   ```yaml
   tp_dbt:
     outputs:
       dev:
         type: duckdb
         path: data/shop_sphere.db  # Stocke les données localement
     target: dev
   ```
3. **Tester la connexion locale** :
   ```sh
   dbt debug
   ```

---

## 📝 Partie 2 - Chargement des données sources
### 📍 Objectif : Charger les fichiers CSV et les transformer en tables exploitables

### 🔹 Étape 3 : Définir les sources de données
1. **Placez les fichiers CSV dans le dossier `seeds/`.**
2. **Déclarez ces fichiers comme sources de données dans DBT.**
3. **Chargez ces fichiers pour les rendre accessibles sous forme de tables locales.**

💡 **Indice** : Les fichiers CSV doivent être déclarés comme `seeds` dans DBT et peuvent être utilisés directement dans les modèles.

1. **Créer un dossier `seeds/` et y placer les fichiers CSV**
2. **Déclarer les sources dans `models/sources.yml`** :
   ```yaml
   version: 2
   sources:
     - name: raw_data
       tables:
         - name: orders
         - name: customers
         - name: products
   ```
3. **Charger les fichiers CSV en tant que tables locales avec DBT** :
   ```sh
   dbt seed
   ```

---

## 📝 Partie 3 - Transformation des données
### 📍 Objectif : Nettoyer et structurer les données

### 🔹 Étape 4 : Création des modèles de staging
1. **Créez des modèles de staging pour chaque source de données (`orders`, `customers`, `products`).**
2. **Assurez-vous que chaque modèle référence correctement les sources.**
3. **Exécutez les modèles et vérifiez les résultats.**

💡 **Aide** : Un modèle de staging est un fichier SQL qui récupère et nettoie les données brutes avant de les transformer.

1. **Créer un modèle `models/staging/stg_orders.sql`** :
   ```sql
   SELECT * FROM {{ source('raw_data', 'orders') }}
   ```
2. **Créer un modèle `models/staging/stg_customers.sql`** :
   ```sql
   SELECT * FROM {{ source('raw_data', 'customers') }}
   ```
3. **Créer un modèle `models/staging/stg_products.sql`** :
   ```sql
   SELECT * FROM {{ source('raw_data', 'products') }}
   ```
4. **Exécuter les modèles** :
   ```sh
   dbt run
   ```

### 🔹 Étape 5 : Création d’un modèle analytique
1. **Créez un modèle `sales_analysis.sql` qui relie les commandes aux clients et aux produits.**
2. **Ajoutez uniquement les colonnes nécessaires à l’analyse des ventes.**
3. **Exécutez ce modèle et validez les résultats.**

💡 **Indice** : Vous devez utiliser `JOIN` pour relier les commandes, les clients et les produits à l’aide des `customer_id` et `product_id`.

1. **Créer un modèle `models/marts/sales_analysis.sql`** :
   ```sql
   SELECT
       o.order_id,
       c.customer_name,
       p.product_name,
       o.quantity,
       o.total_amount,
       o.order_date
   FROM {{ ref('stg_orders') }} o
   JOIN {{ ref('stg_customers') }} c ON o.customer_id = c.customer_id
   JOIN {{ ref('stg_products') }} p ON o.product_id = p.product_id
   ```
2. **Exécuter les modèles** et vérifier la sortie :
   ```sh
   dbt run
   ```

---

## 📝 Partie 4 - Tests et documentation
### 📍 Objectif : Assurer la qualité des transformations

### 🔹 Étape 6 : Ajouter des tests
1. **Ajoutez des tests pour vérifier l’unicité et la présence des valeurs dans les colonnes clés (`order_id`, `customer_id`).**
2. **Exécutez les tests et analysez les résultats.**

💡 **Aide** : Les tests peuvent être définis dans `schema.yml` et exécutés avec DBT.

1. **Déclarer des tests dans `models/schema.yml`** :
   ```yaml
   version: 2
   models:
     - name: stg_orders
       columns:
         - name: order_id
           tests:
             - unique
             - not_null
   ```
2. **Exécuter les tests** :
   ```sh
   dbt test
   ```

### 🔹 Étape 7 : Générer la documentation
1. **Ajoutez des descriptions aux modèles et aux colonnes pour améliorer la documentation.**
2. **Générez la documentation et visualisez-la dans un navigateur.**

💡 **Indice** : DBT permet de générer une documentation interactive pour explorer la structure des données.

1. **Générer la documentation interactive** :
   ```sh
   dbt docs generate
   ```
2. **Lancer un serveur local pour visualiser la documentation** :
   ```sh
   dbt docs serve
   ```

---

## 📝 Partie 5 - Approfondissement : Optimisation et analyses avancées
### 📍 Objectif : Aller plus loin avec DBT

### 🔹 Étape 8 : Ajouter un modèle incrémental
1. **Modifiez `sales_analysis.sql` pour qu’il ne charge que les nouvelles commandes à chaque exécution.**
2. **Exécutez ce modèle plusieurs fois et observez l’évolution des données.**

💡 **Indice** : Utilisez `is_incremental()` pour ne récupérer que les nouvelles lignes depuis la dernière exécution.

1. **Modifier `sales_analysis.sql` pour qu’il charge les nouvelles commandes uniquement** :
   ```sql
   {{ config(materialized='incremental', unique_key='order_id') }}
   
   SELECT * FROM {{ ref('stg_orders') }}
   {% if is_incremental() %}
       WHERE order_date > (SELECT MAX(order_date) FROM {{ this }})
   {% endif %}
   ```
2. **Exécuter** :
   ```sh
   dbt run
   ```

### 🔹 Étape 9 : Ajouter un snapshot pour suivre l’évolution des clients
1. **Créez un snapshot permettant de suivre les modifications des noms des clients au fil du temps.**
2. **Exécutez le snapshot et observez les versions des enregistrements stockées.**

💡 **Aide** : Les snapshots permettent de suivre les changements des données sources en stockant plusieurs versions des enregistrements.

1. **Créer `snapshots/customer_snapshot.sql`** :
   ```sql
   {% snapshot customer_snapshot %}
   
   {{ config(
       target_schema='snapshots',
       unique_key='customer_id',
       strategy='check',
       check_cols=['customer_name']
   ) }}
   
   SELECT * FROM {{ source('raw_data', 'customers') }}
   
   {% endsnapshot %}
   ```
2. **Exécuter** :
   ```sh
   dbt snapshot
   ```

---


## 📝 Partie 6 - Orchestration avec Dagster
### 📍 Objectif : Combiner Dagster et dbt afin de créer des pipelines puissantes et robustes

### 🔹 Étape 10 : Débuter le TP "Dagster & dbt" de dagster university

Rdv ici: https://courses.dagster.io/courses/dagster-dbt
