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

