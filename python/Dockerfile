# Ce Dockerfile construit une image Docker qui contient Python 3, les dépendances Python spécifiées dans le fichier `requirements.txt`, et l'application Flask.

# L'image Docker de base est `python:3`, qui est une image Docker officielle qui contient Python 3.
FROM python:3

# Le répertoire de travail par défaut est `/app`.
WORKDIR /app

# Tous les fichiers et répertoires du répertoire `app/` du système hôte sont copiés vers le répertoire de travail du conteneur Docker.
COPY app/ .

# Les dépendances Python spécifiées dans le fichier `requirements.txt` sont installées dans le conteneur Docker.
# L'option `--no-cache-dir` indique à Pip de ne pas utiliser le cache local, ce qui garantit que les dépendances Python sont toujours installées à partir de la source.
RUN pip install --no-cache-dir -r requirements.txt

# La variable d'environnement `FLASK_APP` est définie avec la valeur `main`.
# Cette variable d'environnement est utilisée par l'application Flask pour spécifier le module principal de l'application.
ENV FLASK_APP="main"

# La commande `python3 -m flask run --host=0.0.0.0` est exécutée lorsque le conteneur Docker est démarré.
# Cette commande démarre l'application Flask en écoute sur toutes les interfaces réseau disponibles.
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
