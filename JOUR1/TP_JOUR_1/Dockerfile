# Utilisation de Python comme image de base
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY scripts/ scripts/
COPY .env .env

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le dossier de données
COPY data/ data/

# Commande d'exécution par défaut
CMD ["sh", "-c", "python scripts/etl.py && tail -f /dev/null"]
