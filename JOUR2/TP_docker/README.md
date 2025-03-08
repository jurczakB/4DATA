# 🚀 TP : Conteneurisation d'un Pipeline de Données avec Docker

## 📌 Partie 1 : Introduction et Mise en Place de Docker

### 🎯 Objectif
L'objectif de cette première partie est de **découvrir Docker**, comprendre ses **concepts fondamentaux**, et **maîtriser les commandes de base**. À la fin de cette section, l’étudiant saura :
- Installer et configurer Docker.
- Comprendre les concepts clés : images, conteneurs, volumes, réseaux.
- Utiliser les commandes Docker essentielles.
- Manipuler et gérer des conteneurs.

---

## 🏗️ 1. Installation de Docker et Docker Compose

### 🔹 Sous Windows / macOS

1. Télécharger **Docker Desktop** : [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. Installer le logiciel en suivant les instructions de l'installateur.
3. Démarrer Docker Desktop et vérifier que Docker fonctionne avec :

   ```sh
   docker --version
   docker-compose --version
   ```

4. Activer **WSL 2 backend** sous Windows si nécessaire (voir la documentation officielle de Docker).

### 🔹 Sous Linux (Ubuntu/Debian)

1. **Mettre à jour le système** :
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
2. **Installer les paquets nécessaires** :
   ```sh
   sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
   ```
3. **Ajouter la clé GPG et le dépôt officiel Docker** :
   ```sh
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   ```
4. **Installer Docker CE (Community Edition)** :
   ```sh
   sudo apt update
   sudo apt install -y docker-ce docker-ce-cli containerd.io
   ```
5. **Vérifier l'installation** :
   ```sh
   docker --version
   docker-compose --version
   ```
6. **Ajouter l'utilisateur actuel au groupe Docker pour éviter d'utiliser `sudo` à chaque commande** :
   ```sh
   sudo usermod -aG docker $USER
   ```
7. **Redémarrer la session** pour appliquer les modifications.

---

## 🔍 2. Concepts Clés de Docker

### 🛠️ Image Docker

Une **image Docker** est un modèle utilisé pour créer un conteneur. Elle contient tout le nécessaire pour exécuter une application :

- Système de fichiers.
- Dépendances.
- Code source.

**Commande pour télécharger une image** :
```sh
docker pull nginx
```

**Lister les images disponibles** :
```sh
docker images
```

**Supprimer une image** :
```sh
docker rmi <image_id>
```

### 📦 Conteneur Docker

Un **conteneur** est une instance exécutable d’une image. Il peut être démarré, arrêté et supprimé sans affecter l’image de base.

**Créer et exécuter un conteneur** :
```sh
docker run -d --name my_nginx -p 8080:80 nginx
```

**Lister les conteneurs en cours d’exécution** :
```sh
docker ps
```

**Arrêter et supprimer un conteneur** :
```sh
docker stop my_nginx

docker rm my_nginx
```

### 🛜 Réseaux Docker

Docker utilise des réseaux pour permettre aux conteneurs de communiquer entre eux.

**Lister les réseaux existants** :
```sh
docker network ls
```

**Créer un réseau personnalisé** :
```sh
docker network create my_network
```

**Démarrer un conteneur en l’attachant à un réseau** :
```sh
docker run -d --name my_app --network my_network nginx
```

### 📂 Volumes et Persistance des Données

Les **volumes Docker** permettent de stocker des données qui persistent après l'arrêt d'un conteneur.

**Créer un volume** :
```sh
docker volume create my_volume
```

**Monter un volume dans un conteneur** :
```sh
docker run -d -v my_volume:/app/data --name data_container nginx
```

**Vérifier l’utilisation des volumes** :
```sh
docker volume ls
```

---

## 🚀 3. Exercices Pratiques

### Exercice 1 : Création et manipulation d’un conteneur

✅ Téléchargez et exécutez une image Alpine Linux en mode interactif :
```sh
docker run -it alpine sh
```
✅ Testez quelques commandes Linux à l’intérieur du conteneur (ex: `ls`, `pwd`, `echo "Hello Docker"`).
✅ Sortez du conteneur (`exit`) et essayez de le redémarrer :
```sh
docker start <container_id>
```
✅ Supprimez le conteneur et l’image.

---

### Exercice 2 : Déploiement d’un serveur web Nginx

✅ **Lancez un serveur Nginx** exposé sur le port 8080 :
```sh
docker run -d --name webserver -p 8080:80 nginx
```
✅ **Ouvrez un navigateur et accédez à** `http://localhost:8080`.
✅ **Modifiez la page d’accueil** en créant un volume :
```sh
docker run -d --name webserver -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html nginx
```
✅ **Vérifiez que les changements sont appliqués**.

---

📌 **Dans cette première partie, nous avons appris à :**

✅ Installer Docker et Docker Compose.
✅ Comprendre les concepts fondamentaux : images, conteneurs, volumes, réseaux.
✅ Exécuter et manipuler des conteneurs avec les commandes essentielles.
✅ Déployer un serveur web avec Docker.

🔜 **Dans la partie suivante**, nous allons **conteneuriser une base de données** et la rendre persistante. 🚀

---

## 3. Conteneurisation d'une Base de Données

### Objectif

L'objectif de cette section est d'apprendre à **déployer et gérer une base de données relationnelle dans un conteneur Docker**. Points clés

- Déployer une base de données relationnelle (PostgreSQL, MySQL...)
- Configurer la persistance des données avec Docker Volumes
- Se connecter à la base depuis un client SQL
- Sécuriser la base de données

### Instructions

1. **Choisir une base de données**

   - Rechercher une image officielle Docker pour une base de données comme PostgreSQL ou MySQL.
   - Lire la documentation pour comprendre les variables d’environnement nécessaires (ex: utilisateur, mot de passe, nom de la base).

2. **Lancer un conteneur pour la base de données**

   - Démarrer un conteneur en exposant les ports et en définissant les paramètres de connexion.
   - Vérifier que le conteneur est bien en cours d’exécution.

3. **Tester la connexion à la base de données**

   - Se connecter avec un client SQL (ex: `psql` pour PostgreSQL, `mysql` pour MySQL).
   - Créer une table et insérer des données.
   - Vérifier la persistance des données après le redémarrage du conteneur.

4. **Ajouter la persistance des données**

   - Modifier le conteneur pour stocker les données dans un volume Docker.
   - Tester la récupération des données après l’arrêt et la relance du conteneur.

5. **Sécurisation de la base de données**

   - Définir des règles d’accès restrictives.
   - Scanner les vulnérabilités de l’image Docker utilisée.
   - Tester l’accès distant et les configurations réseau.

### Pistes et Indices

- Pour trouver l’image officielle, consultez Docker Hub : [https://hub.docker.com/](https://hub.docker.com/)
- Vérifiez les logs du conteneur pour résoudre les erreurs :
  ```sh
  docker logs <nom_du_conteneur>
  ```
- Testez la connexion avec un client SQL comme `pgAdmin` pour PostgreSQL ou `MySQL Workbench` pour MySQL.
- Utilisez les volumes pour garantir la persistance des données :
  ```sh
  docker volume create my_db_volume
  ```

---


## 4. Conteneurisation d’un Service de Traitement de Données

### Objectif
L’objectif de cette partie est d’apprendre à **conteneuriser un service de traitement de données** qui interagit avec la base de données créée précédemment. 
Points clés:
- Développer un **script Python** capable d’extraire des données depuis la base de données conteneurisée.
- Transformer ces données et générer un **fichier de sortie** (CSV, JSON, etc.).
- Intégrer ce service dans un conteneur Docker.
- Configurer l’exécution de ce service de manière orchestrée avec Docker Compose.

---

### Instructions

#### 1. Développement du service de traitement de données
- Écrire un script Python (`etl.py`) permettant de :
  - Se connecter à la base de données via une **bibliothèque adaptée** (ex: `psycopg2` pour PostgreSQL, `mysql-connector` pour MySQL).
  - Lire les données d’une table et les transformer (ex: filtrage, normalisation, enrichissement).
  - Enregistrer les résultats dans un fichier (CSV, JSON).
- Utiliser un fichier de configuration (`.env`, `config.json`) pour stocker les informations de connexion.

#### 2. Conteneurisation du service
- Définir un `Dockerfile` permettant :
  - D’installer **Python** et les dépendances nécessaires.
  - D’intégrer le script et ses fichiers dans un conteneur Docker.
  - De s’assurer que le service démarre correctement à l’exécution du conteneur.

#### 3. Intégration avec Docker Compose
- Ajouter un service `etl` dans le fichier `docker-compose.yml`.
- Vérifier que le service démarre **après** la base de données.
- Configurer un volume si le service génère un fichier de sortie.

#### 4. Test et validation
- Lancer le service et vérifier qu’il interagit correctement avec la base de données.
- Vérifier la présence des fichiers de sortie générés.
- Inspecter les logs du conteneur pour identifier d’éventuelles erreurs.

---

### Pistes et Indices
- Consultez la documentation officielle de **Docker Hub** pour identifier l’image Python la plus adaptée.
- Vérifiez que le service attend que la base de données soit **prête** avant d’exécuter les requêtes SQL.
- Pour lire et écrire des fichiers dans un conteneur, pensez aux **volumes Docker**.
- Pour éviter d’exposer les informations sensibles dans le code, utilisez un fichier `.env` et chargez les variables d’environnement.
- Utilisez `docker-compose logs -f <nom_du_service>` pour déboguer les erreurs en temps réel.

---

## 5. : Sécurisation et Optimisation

### Objectif
L’objectif de cette dernière partie est de **sécuriser et optimiser l’exécution des conteneurs** afin de garantir un pipeline fiable, performant et résistant aux attaques. Points clés:
- Mettre en place des **bonnes pratiques de sécurité** pour protéger les services conteneurisés.
- Scanner les vulnérabilités des images Docker.
- Gérer les **secrets et accès** pour éviter l’exposition d’informations sensibles.
- Optimiser l’utilisation des ressources pour améliorer les performances.

---

### Instructions

#### 1. Sécurisation des Conteneurs
- Vérifier les permissions des fichiers et des utilisateurs à l’intérieur des conteneurs.
- Restreindre l’utilisation des privilèges **root** dans les images Docker.
- Utiliser des images minimales pour réduire la surface d’attaque.
- Scanner les images Docker pour identifier les vulnérabilités et les paquets obsolètes.

#### 2. Gestion des Secrets et Accès
- Ne pas stocker les mots de passe et clés API directement dans le code source.
- Utiliser des fichiers `.env` pour stocker les credentials et les injecter dans les conteneurs.
- Explorer des solutions comme **Docker Secrets** ou **Vault** pour la gestion sécurisée des secrets.
- Vérifier et restreindre les permissions d’accès réseau des conteneurs.

#### 3. Optimisation des Performances
- Limiter l’utilisation des ressources CPU et mémoire avec des paramètres de contrainte Docker.
- Configurer des **volumes optimisés** pour améliorer la persistance des données.
- Activer la mise en cache dans les `Dockerfile` pour accélérer la construction des images.
- Analyser la consommation de ressources des conteneurs avec des outils comme `docker stats`.

#### 4. Surveillance et Logging
- Mettre en place un système de **monitoring** pour observer l’état des conteneurs.
- Configurer des logs centralisés pour suivre les erreurs et événements anormaux.
- Automatiser les alertes en cas d’anomalie sur les services conteneurisés.

---

### Pistes et Indices
- Explorez l’outil **Trivy** pour scanner les images Docker et détecter des vulnérabilités.
- Utilisez `docker inspect <nom_du_conteneur>` pour analyser la configuration et les accès du conteneur.
- Testez les limites de ressources avec des commandes comme :
  ```sh
  docker run --memory=512m --cpus=1 my_service
  ```
- Consultez la documentation officielle sur **Docker Secrets** et **Kubernetes Secrets** pour sécuriser les données sensibles.
- Activez un monitoring avec **Prometheus** ou **Grafana** pour visualiser la charge des conteneurs.

---

## 6. Conteneurisation Complète du Cycle ETL

### Objectif
L’objectif de cette partie est de **conteneuriser entièrement un pipeline de traitement de données ETL** réalisé dans le TP précédent. 
Points clés:
- Conteneuriser chaque étape du pipeline (extraction, transformation, chargement, visualisation).
- Utiliser **Docker Compose** pour orchestrer l’exécution des services.
- Assurer la persistance des données et la communication entre les services.
- Optimiser l’exécution et garantir la sécurité du pipeline conteneurisé.

---

### Instructions

#### 1. Conteneurisation des différentes étapes
- Chaque étape du pipeline (extraction, transformation, chargement, visualisation) doit être intégrée dans un **conteneur Docker** distinct.
- Définir un `Dockerfile` pour chaque service avec les dépendances nécessaires.

#### 2. Orchestration avec Docker Compose
- Définir un fichier `docker-compose.yml` permettant d’orchestrer l’exécution du pipeline.
- Configurer les dépendances entre services pour garantir une exécution correcte.
- Définir des **volumes persistants** pour conserver les données entre les exécutions.

#### 3. Optimisation et Sécurisation
- Restreindre les accès et éviter les exécutions en mode **root**.
- Utiliser des **réseaux Docker** pour contrôler la communication entre les services.
- Tester le pipeline conteneurisé et optimiser son exécution.

---

### Pistes et Indices
- Vérifiez la connexion entre les services avec `docker network ls`.
- Utilisez `depends_on` dans `docker-compose.yml` pour gérer les dépendances.
- Testez chaque service individuellement avant l’exécution complète.

---

