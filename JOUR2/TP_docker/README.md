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

## 🎯 4. Récapitulatif et Prochaines Étapes

📌 **Dans cette première partie, nous avons appris à :**

✅ Installer Docker et Docker Compose.
✅ Comprendre les concepts fondamentaux : images, conteneurs, volumes, réseaux.
✅ Exécuter et manipuler des conteneurs avec les commandes essentielles.
✅ Déployer un serveur web avec Docker.

🔜 **Dans la partie suivante**, nous allons **conteneuriser une base de données** et la rendre persistante. 🚀

---

**📢 Besoin d’aide ?**
Consultez la documentation officielle : [Docker Docs](https://docs.docker.com/)

💡 **Bon apprentissage !** 🎉

