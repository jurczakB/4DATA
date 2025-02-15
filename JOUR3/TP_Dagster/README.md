# Aperçu du Projet

Dans ce cours, nous allons nous concentrer sur les orchestrateurs axés sur les assets et sur la manière dont ils simplifient la gestion des pipelines de données. Vous allez utiliser **Dagster**, un orchestrateur open-source, pour construire un pipeline de données exemple.

À l'aide des données issues de **NYC OpenData**, vous allez créer un pipeline de données qui :

- **Extrait** les données stockées dans des fichiers Parquet depuis NYC OpenData.
- **Charge** ces données dans une base de données **DuckDB**.
- **Transforme** et prépare les données pour l'analyse.
- **Crée une visualisation** à partir des données transformées.

Si vous êtes bloqué ou souhaitez avancer plus rapidement, consultez le projet finalisé disponible sur **GitHub**.

---

## Prérequis

Pour installer **Dagster**, vous aurez besoin de :

- **Installer Python**. Dagster prend en charge **Python 3.9 à 3.12**.
- Un **gestionnaire de paquets** comme **pip**, **Poetry** ou **uv**. Si vous devez installer un gestionnaire de paquets, consultez les guides d'installation suivants :
  - [pip](https://pip.pypa.io/en/stable/installation/)
  - [Poetry](https://python-poetry.org/docs/#installation)
  - [uv](https://github.com/astral-sh/uv)

Pour vérifier si **Python** et le **gestionnaire de paquets** sont déjà installés dans votre environnement, exécutez :

```sh
python --version
pip --version
```

---

## Installation

💡 **Remarque** : Nous recommandons fortement d'installer Dagster dans un **environnement virtuel Python**. Si vous avez besoin d'un rappel sur la création et l'activation d'un environnement virtuel, consultez [cet article de blog](https://realpython.com/python-virtual-environments-a-primer/).

Pour installer **Dagster** dans votre environnement Python actuel, exécutez la commande suivante :

```sh
pip install dagster~=1.9
```

---

## Création du projet Dagster

Créons votre premier projet Dagster ! Pour cela, utilisez la commande `dagster project from-example` afin de cloner le projet officiel **Dagster University** sur votre machine locale.

Pour créer le projet, exécutez :

```sh
dagster project from-example --example project_dagster_university_start --name dagster_university
```

Après l'exécution de cette commande, un nouveau répertoire nommé **dagster_university** sera créé dans votre répertoire actuel. Ce répertoire contiendra les fichiers constituant votre projet Dagster.

Ensuite, configurez les variables d'environnement par défaut et installez les dépendances Python du projet en exécutant :

```sh
cd dagster_university
cp .env.example .env
pip install -e ".[dev]"
```

L'option `-e` installe le projet en mode **éditable**, ce qui améliore l'expérience de développement en réduisant le temps nécessaire pour tester une modification. Les principales exceptions sont l'ajout de nouveaux assets ou l'installation de dépendances supplémentaires.

Pour vérifier que l'installation a réussi et que vous pouvez exécuter Dagster en local, lancez :

```sh
dagster dev
```

Naviguez vers **[localhost:3000](http://localhost:3000)**, où vous devriez voir l'interface utilisateur de Dagster.

💡 **Remarque** : La commande `dagster dev` exécutera Dagster en continu jusqu'à ce que vous l'arrêtiez. Pour arrêter le processus en cours d'exécution, utilisez **Control + C** dans le terminal.

---

## Définition de votre premier asset

Dans ce cours, vous utiliserez les données de **NYC OpenData** pour analyser les trajets en taxi à New York. Le premier asset que vous allez définir utilise les données de **TLC Trip Record Data**, qui contient les enregistrements de trajets pour plusieurs types de véhicules. Nous nous concentrerons sur les taxis jaunes.

Votre premier asset, nommé `taxi_trips_file`, va récupérer les données des taxis jaunes pour **mars 2023** et les enregistrer localement.

1. **Ouvrir le fichier `assets/trips.py`** dans votre projet Dagster.
2. **Vérifier que les imports suivants existent déjà** en haut du fichier :

```python
import requests
from . import constants
```

3. **Définir une fonction qui récupère les données et les sauvegarde localement** :

```python
def taxi_trips_file() -> None:
    """
    Récupère les fichiers Parquet bruts des trajets en taxi.
    Sourced from the NYC Open Data portal.
    """
    month_to_fetch = '2023-03'
    raw_trips = requests.get(
        f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_to_fetch}.parquet"
    )

    with open(constants.TAXI_TRIPS_TEMPLATE_FILE_PATH.format(month_to_fetch), "wb") as output_file:
        output_file.write(raw_trips.content)
```

4. **Transformer cette fonction en un asset Dagster** :

    - **Importer `asset` depuis la bibliothèque Dagster** :

    ```python
    from dagster import asset
    ```

    - **Ajouter le décorateur `@asset` avant la fonction** :

    ```python
    @asset
    def taxi_trips_file() -> None:
        """
        Récupère les fichiers Parquet bruts des trajets en taxi.
        """
        month_to_fetch = '2023-03'
        raw_trips = requests.get(
            f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_to_fetch}.parquet"
        )

        with open(constants.TAXI_TRIPS_TEMPLATE_FILE_PATH.format(month_to_fetch), "wb") as output_file:
            output_file.write(raw_trips.content)
    ```

C'est tout ! 🎉 Vous venez de créer votre premier **asset Dagster**. En utilisant le décorateur `@asset`, vous pouvez facilement transformer une fonction Python en un asset Dagster.

ℹ️ **Note sur `-> None`** : Il s'agit d'une **annotation de type** en Python indiquant que la fonction ne retourne rien. L'utilisation des annotations de type est fortement recommandée pour rendre le code plus lisible et compréhensible.


---

## Matérialisation de votre asset

Une fois votre asset défini dans le code, l'étape suivante consiste à le **matérialiser**. Lorsqu'un asset est matérialisé, Dagster exécute la fonction associée et enregistre le résultat dans un stockage, comme un entrepôt de données.

### Exécution de la matérialisation via l'interface Dagster

Si vous n'avez pas encore l'interface **Dagster UI** en cours d'exécution, démarrez-la en exécutant la commande suivante à la racine de votre projet Dagster :

```sh
dagster dev
```

Puis, accédez à **[localhost:3000](http://localhost:3000)** dans votre navigateur.

1. **Cliquez sur "Assets" dans la barre de navigation supérieure**. Vous verrez la liste des assets disponibles dans le projet.
2. **Si la page est vide, cliquez sur "Reload definitions"** pour recharger les définitions des assets.
3. **Cliquez sur "View global asset lineage"** pour visualiser la hiérarchie de votre asset.
4. **Cliquez sur le bouton "Materialize"** pour exécuter la fonction de l'asset et générer le fichier de données.
5. **Une boîte de notification violette apparaîtra**, indiquant que l'exécution a démarré avec succès.
6. **Une fois la matérialisation terminée**, accédez au répertoire `data/raw/` dans votre projet et vérifiez la présence du fichier généré :

```sh
ls data/raw/taxi_trips_2023-03.parquet
```

💡 **Remarque** : Le téléchargement du fichier peut prendre quelques instants.

C'est tout ! 🎉 Vous avez maintenant **matérialisé votre premier asset** avec Dagster !

---

## Consultation des détails d'exécution

Maintenant que vous avez matérialisé un asset, il est essentiel de savoir comment consulter les détails d'exécution.

1. **Localiser l'exécution de la matérialisation**
   - Dans l'interface **Dagster UI**, repérez la section **Materialized - <DATE>** sur la page de l'asset.
   - Cliquez sur la **date** mise en évidence pour accéder à la page de détails d'exécution.

2. **Consulter les logs et informations**
   - La page affichera des informations sur l'exécution, y compris les **logs**, les **statuts d'exécution**, et les éventuelles **erreurs**.
   - Vous pouvez utiliser ces détails pour **identifier et résoudre d'éventuels problèmes**.

Si votre exécution avait échoué, cette page vous aiderait à diagnostiquer la cause et à ajuster votre code en conséquence. Parcourez la afin de vous familiariser avec l'UI et un potentiel débuggage...

---

## Dépannage des exécutions échouées

Si un asset échoue lors de sa matérialisation, vous pouvez identifier la cause et corriger l'erreur en suivant ces étapes :

1. **Déclencher une erreur intentionnelle**
   - Modifiez `assets/trips.py` en commentant l'importation de `constants`.
   - Lancez la matérialisation dans **Dagster UI** et observez l'échec.

2. **Analyser les logs d'exécution**
   - Ouvrez les **Run details** et repérez le statut **Failure**.
   - Identifiez l'étape en échec via le message d'erreur dans les logs.

3. **Corriger l'erreur**
   - Réactivez l'importation de `constants` dans `trips.py` et enregistrez.
   - Fermez la fenêtre d'erreur dans **Dagster UI**.

4. **Relancer l'exécution**
   - Cliquez sur **Re-execute all** dans **Dagster UI** pour relancer toutes les étapes.
   - Vérifiez que la matérialisation aboutit avec succès.

Ces étapes vous permettront de comprendre comment utiliser les logs et les outils de Dagster pour diagnostiquer et corriger les erreurs efficacement.

---

## Création d'un asset taxi_zones_file

Pour mettre en pratique ce que vous avez appris, créez un nouvel asset dans `trips.py` qui :

- **Est nommé `taxi_zones_file`**, qui contiendra un identifiant unique et le nom de chaque zone de taxi à New York.
- **Utilise la bibliothèque `requests`** pour récupérer les données depuis l'URL suivante :
  
  `https://community-engineering-artifacts.s3.us-west-2.amazonaws.com/dagster-university/data/taxi_zones.csv`
  
- **Stocke les données sous forme de fichier CSV** dans `data/raw/taxi_zones.csv`. Le chemin est défini dans `constants.TAXI_ZONES_FILE_PATH`.

Une fois cet asset créé et ajouté à votre projet, vous pourrez le matérialiser de la même manière que l'asset précédent en utilisant l'interface **Dagster UI**.

---

## Création d'un pipeline de données

Jusqu'ici, nous avons vu ce qu'est un asset et comment en créer dans Dagster. Maintenant, nous allons étendre votre projet Dagster pour construire un pipeline de données.

Les pipelines de données sont une suite d'événements produisant des assets. Dagster permet de créer efficacement ces pipelines tout en gérant plusieurs assets interdépendants.

Vous allez maintenant construire un pipeline complet qui :

- **Charge les fichiers téléchargés dans une base de données**.
- **Combine et agrège les données** pour générer des métriques sur les trajets en taxi.
- **Visualise ces métriques et enregistre un rapport**.

Pendant ce processus, vous apprendrez à définir des dépendances entre assets pour structurer vos pipelines efficacement.

---

## Exécution des assets et base de données

Précédemment, nous avons créé deux assets indépendants : `taxi_trips_file` et `taxi_zones_file`. Maintenant, nous allons créer de nouveaux assets qui dépendent de ces fichiers de données.

Avant de travailler avec ces fichiers, il est préférable de les charger dans une base de données pour améliorer l'efficacité et le stockage. Heureusement, le projet est configuré avec **DuckDB**, une base de données intégrée qui facilite l'ingestion et la requête de données.

DuckDB permet notamment d'exécuter des requêtes SQL directement sur des fichiers. Par exemple, pour charger le fichier `taxi_trips_file` dans DuckDB, on pourrait exécuter la requête SQL suivante :

```sql
CREATE OR REPLACE TABLE trips AS (
    SELECT
        VendorID AS vendor_id,
        PULocationID AS pickup_zone_id,
        DOLocationID AS dropoff_zone_id,
        RatecodeID AS rate_code_id,
        payment_type AS payment_type,
        tpep_dropoff_datetime AS dropoff_datetime,
        tpep_pickup_datetime AS pickup_datetime,
        trip_distance AS trip_distance,
        passenger_count AS passenger_count,
        total_amount AS total_amount
    FROM 'data/raw/taxi_trips_2023-03.parquet'
);
```

Nous verrons dans la prochaine section comment exécuter cette requête et intégrer ce chargement dans Dagster.

---

## Chargement des données dans la base de données

Maintenant que nous avons défini une requête SQL permettant de charger les données dans **DuckDB**, nous allons utiliser **Dagster** pour gérer la matérialisation de ces assets. En déléguant cette tâche à Dagster, nous pouvons facilement suivre l'évolution des tables et mesurer le temps d'exécution.

### Définition de l'asset `taxi_trips`

Ajoutez le code suivant à la fin du fichier `trips.py` :

```python
import duckdb
import os
from dagster import asset
from dagster._utils.backoff import backoff

@asset(
    deps=["taxi_trips_file"]
)
def taxi_trips() -> None:
    """
    Le jeu de données brut des trajets en taxi, chargé dans une base de données DuckDB.
    """
    query = """
        CREATE OR REPLACE TABLE trips AS (
          SELECT
            VendorID AS vendor_id,
            PULocationID AS pickup_zone_id,
            DOLocationID AS dropoff_zone_id,
            RatecodeID AS rate_code_id,
            payment_type AS payment_type,
            tpep_dropoff_datetime AS dropoff_datetime,
            tpep_pickup_datetime AS pickup_datetime,
            trip_distance AS trip_distance,
            passenger_count AS passenger_count,
            total_amount AS total_amount
          FROM 'data/raw/taxi_trips_2023-03.parquet'
        );
    """

    conn = backoff(
        fn=duckdb.connect,
        retry_on=(RuntimeError, duckdb.IOException),
        kwargs={
            "database": os.getenv("DUCKDB_DATABASE"),
        },
        max_retries=10,
    )
    conn.execute(query)
```

### Explication du code

- **Le décorateur `@asset`** : Permet à Dagster de reconnaître `taxi_trips` comme un asset.
- **Dépendance `deps=["taxi_trips_file"]`** : Assure que `taxi_trips_file` est matérialisé avant `taxi_trips`.
- **Requête SQL** : Crée ou remplace la table `trips` en important les données du fichier `taxi_trips_file`.
- **Connexion sécurisée avec `backoff`** : Permet d'éviter des conflits d'accès multiples à DuckDB.

### Rechargement des définitions

Après avoir ajouté ce nouvel asset, vous devez **recharger les définitions** dans **Dagster UI** :

1. Ouvrez **Dagster UI**.
2. Cliquez sur **"Reload Definitions"**.
3. Vérifiez que `taxi_trips` apparaît dans le graphe des assets avec une flèche indiquant sa dépendance à `taxi_trips_file`.

### Matérialisation du pipeline

Dans **Dagster UI**, cliquez sur **"Materialize all"** pour lancer l'exécution des assets :

- **`taxi_trips_file` et `taxi_zones_file` sont exécutés en parallèle**.
- **`taxi_trips` attend que `taxi_trips_file` soit complété** avant d'être matérialisé.

Cela est possible grâce à la déclaration de dépendance `deps=["taxi_trips_file"]`.

### Vérification de la matérialisation

Pour confirmer que les données ont bien été chargées dans DuckDB, ouvrez un terminal et exécutez les commandes suivantes :

```python
import duckdb
conn = duckdb.connect(database="data/staging/data.duckdb")
conn.execute("SELECT COUNT(*) FROM trips").fetchall()
```

Si tout s'est bien passé, cette commande affichera le nombre de trajets de taxi ingérés.

🚀 **Félicitations !** Vous avez maintenant construit un pipeline de données complet qui récupère des données depuis une API et les stocke dans une base de données pour analyse.

---  

### Pratique : Création d'un asset `taxi_zones`

En utilisant vos connaissances sur la gestion des dépendances entre assets, créez un asset `taxi_zones` qui utilise `taxi_zones_file` pour générer une table `zones` dans DuckDB.

Cet asset doit :

- **S'appeler `taxi_zones`**.
- **Utiliser le fichier `taxi_zones_file`** comme source de données.
- **Créer une table `zones` dans DuckDB** avec les colonnes suivantes :
  - `zone_id`, correspondant à `LocationID`, renommé.
  - `zone`.
  - `borough`.
  - `geometry`, correspondant à `the_geom`, renommé.

### Instructions

1. Modifiez le fichier `trips.py` pour ajouter l'asset `taxi_zones`.
2. Assurez-vous que `taxi_zones_file` est correctement référencé comme dépendance.
3. Utilisez une requête SQL pour transformer et charger les données dans DuckDB.
4. Rechargez les définitions dans **Dagster UI**.
5. Matérialisez l'asset `taxi_zones` après `taxi_zones_file`.
6. Vérifiez que la table `zones` a bien été créée dans DuckDB.

💡 **Astuce** : Utilisez Dagster UI pour suivre les dépendances et vous assurer que la matérialisation s'exécute correctement.

