# 🚀 Projet : Implémentation d'une Pipeline de Données avec Dagster

## 📌 Objectif du Projet
L'objectif de ce projet est de concevoir et déployer une pipeline de données **de bout en bout** en utilisant **Dagster** comme orchestrateur. Cette pipeline suivra un processus **ETL (Extract, Transform, Load) ou ELT (Extract, Load, Transform)** afin de récupérer, traiter, stocker et exploiter des données issues d'une API.

## 📋 Cahier des Charges
### 🔹 1. Extraction des Données
- Récupérer des données à partir d'une **API externe** (exemple : API de Météo France, mais libre choix de la source de données pertinente).
- Gérer la récupération des données avec Dagster.

### 🔹 2. Stockage des Données
- Stocker les données dans une **base de données** (PostgreSQL, DuckDB ou autre choix pertinent).

### 🔹 3. Transformation et Exploitation des Données
- Réaliser des **visualisations** basiques : tableaux de bord, graphiques, etc.
- Mettre en place des outils **d'aide à la décision** (exemple : reporting, analyse des tendances, etc.).
- Optionnel : Intégrer un modèle de **Machine Learning ou IA** pour une analyse avancée des données.

### 🔹 4. Orchestration avec Dagster
Le pipeline devra inclure les éléments clés de **Dagster** :
- **Assets** : gestion des ressources et des transformations.
- **Jobs** : définition des étapes du pipeline.
- **Schedules** : exécutions planifiées.
- **Sensors** : détection d'événements pour déclencher des tâches.
- **Partitions** : gestion de la fréquence des traitements et des segments de données.

### 🔹 5. Tests et Monitoring
- Implémenter des **tests unitaires** avec `pytest` pour garantir la fiabilité du code et des transformations de données.
- Ajouter un **monitoring** pour assurer le suivi et le débogage de la pipeline (exemple : logs détaillés, dashboards de suivi, alertes en cas d'erreurs, etc.).

### 🔹 6. Conteneurisation (Bonus)
Un **bonus conséquent** sera attribué si le projet est conteneurisé avec **Docker** pour une meilleure portabilité et déploiement.

## 🛠️ Livrables
### 📌 Code Source
- Le projet devra être versionné sous **Git** et inclure un **README détaillé** expliquant :
  - Les choix de conception.
  - Les étapes d'installation et de déploiement.
  - Les instructions pour exécuter la pipeline.

### 🎤 Soutenance
- Une **présentation et démonstration** du projet devant les encadrants.

## 👥 Modalités de Travail
- **Travail en binôme**.
- Organisation et planification à définir entre les membres de l'équipe.

## 🚀 Déroulement du Projet
1. **Choix de l'API et conception du pipeline**
2. **Mise en place de l'extraction et du stockage des données**
3. **Développement des transformations et visualisations**
4. **Orchestration avec Dagster**
5. **Ajout des tests et du monitoring**
6. **(Optionnel) Conteneurisation du projet**
7. **Finalisation et préparation de la soutenance**

## 🔗 Ressources Utiles
- [Documentation officielle Dagster](https://docs.dagster.io/)
- [API Météo France](https://donneespubliques.meteofrance.fr/)
- [Guide PostgreSQL](https://www.postgresql.org/docs/)
- [Tutoriel Docker](https://docs.docker.com/get-started/)
- [pytest Documentation](https://docs.pytest.org/en/latest/)

Bonne chance et bon développement ! 🚀