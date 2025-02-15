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

## Structure des fichiers du projet

Maintenant que vous avez créé le projet Dagster, voici un aperçu des fichiers qu'il contient :

```
.
├── README.md
├── dagster_university/
│   ├── assets/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── metrics.py
│   │   └── trips.py
│   ├── jobs/
│   ├── partitions/
│   ├── resources/
│   ├── schedules/
│   ├── sensors/
│   └── __init__.py
├── dagster_university_tests
├── data/
│   ├── outputs/
│   ├── raw/
│   ├── requests/
│   │   └── README.md
│   └── staging/
├── .env
├── .env.example
├── pyproject.toml
├── setup.cfg
└── setup.py
```

### Explication des fichiers principaux

| Fichier/Répertoire | Contexte | Description |
|--------------------|----------|-------------|
| `README.md` | Python | Une description et un guide de démarrage du projet Dagster. |
| `dagster_university/` | Dagster | Contient le code Dagster, y compris les assets et capteurs. |
| `dagster_university/__init__.py` | Dagster | Fichier définissant la structure du projet. |
| `dagster_university/assets/constants.py` | Dagster U | Contient des constantes utilisées dans le projet. |
| `dagster_university_tests/` | Dagster | Contient les tests unitaires pour le projet. |
| `data/` | Dagster U | Contient les données manipulées par le projet. |
| `.env` | Python | Fichier contenant les variables d'environnement. |
| `pyproject.toml` | Python | Définit les métadonnées du projet et ses dépendances. |
| `setup.py` | Python | Script pour la gestion des dépendances du projet. |
| `setup.cfg` | Python | Contient les configurations par défaut pour `setup.py`. |

Pour plus d'informations sur ces fichiers et leur rôle dans Dagster, consultez la [documentation officielle](https://docs.dagster.io/).
