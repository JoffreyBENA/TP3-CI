# TP3-CI

Description des fichiers fournis

    1- Jenkinsfile: Ce fichier contient la définition du pipeline d'intégration continue pour les applications Python pour une utilisation avec Jenkins.
    2- .gitlab-ci.yml: Ce fichier contient la définition du pipeline d'intégration continue pour les applications Python pour une utilisation avec GitLab CI.
    3- main.yml: Ce fichier contient la définition du pipeline d'intégration continue pour les applications Python pour une utilisation avec GitHub Actions.
    4- Dockerfile: Ce fichier est utilisé pour construire l'image Docker de l'application Python. Il définit les étapes pour installer les dépendances et lancer l'application dans un conteneur.
    5- requirements.txt: Ce fichier contient la liste des dépendances Python requises pour exécuter l'application.
    6- .flake8: Ce fichier de configuration est utilisé par le linter Flake8 pour définir les règles de formatage et de qualité du code
    7- pytest.ini: Ce fichier de configuration est utilisé par pytest pour personnaliser les options de test.

Pré-requis :

Avant de mettre en place la chaîne d'intégration continue, assurez-vous d'avoir les éléments suivants :

    1- Un système d'automatisation des tâches, tel que Jenkins, GitLab CI ou GitHub Actions, installé et configuré sur votre infrastructure.
    2- Un dépôt Git contenant votre application Python. Assurez-vous d'avoir les droits d'accès nécessaires pour récupérer le code source à partir du dépôt.
    3- Une connexion au Docker Hub avec un identifiant et un mot de passe valides pour pouvoir pousser l'image Docker construite pendant le pipeline.
    4- Les dépendances et outils suivants doivent être installés sur votre système :
        - Python (version compatible avec votre application)
        - Docker
        - pytest
        - flake8
        - clone_digger (pour la vérification des copier-coller)
        - radon (pour l'analyse de la complexité cyclomatique)

Schéma de présentation des étapes du pipeline :

Voici un schéma représentant les différentes étapes du pipeline d'intégration continue pour les applications Python :

                   +---------------------+
                   |   Récupération du   |
                   |     code source     |
                   |     (GitHub)        |
                   +----------+----------+
                              |
                              v
                   +----------+----------+
                   |     Linter de la    |
                   |   qualité du code   |
                   |       (Flake8)      |
                   +----------+----------+
                              |
                              v
            +-----------------+-----------------+
            |   Vérification des copier-coller  |
            |           clone-digger            |
            +-----------------+-----------------+
                              |
                              v
     +------------------------+------------------------+
     |   Analyse de la complexité cyclomatique (Radon) |
     +------------------------+------------------------+
                              |
                              v
             +----------------+----------------+
             |          Tests unitaires        |
             |         (Pytest,Unittest)       |
             +----------------+----------------+
                              |
                              v
              +---------------+--------------+
              |   Construction de l'image    |
              |       Docker (Build)         |
              +---------------+--------------+
                              |
                              v
          +-------------------+-------------------+
          |  Pousser l'image Docker sur le Docker |
          |                  Hub (Push)           |
          +-------------------+-------------------+
                              |
                              v
                   +----------+----------+
                   |    Déploiement      |
                   +---------------------+

Ce schéma présente les différentes étapes du pipeline d'intégration continue pour une application Python. Il commence par la récupération du code source à partir d'un référentiel Git, puis passe par les étapes de linter (vérification des normes de codage), de détection de copier-coller, d'analyse de la complexité cyclomatique, de tests unitaires et enfin de construction et de publication de l'image Docker sur le DOcker Hub.

Configuration des paramètres de pipeline :

Le pipeline d'intégration continue peut être configuré en modifiant certains paramètres. Voici les paramètres pouvant être personnalisés :

    1- URL du dépôt Git : Dans le fichier de pipeline (Jenkinsfile, .gitlab-ci.yml ou .github/workflows/main.yml), vous devez spécifier l'URL du dépôt Git contenant votre application Python. Assurez-vous de mettre à jour cette URL avec celle de votre dépôt.
    2- Paramètres des outils d'analyse de qualité : Certains outils d'analyse de qualité tels que Flake8, clone_digger et radon peuvent nécessiter des fichiers de configuration spécifiques. Assurez-vous de mettre à jour les chemins vers ces fichiers de configuration dans le pipeline en fonction de votre structure de répertoire.
    3- Chemin des tests unitaires : Dans le fichier de configuration des tests (pytest.ini), assurez-vous de spécifier le chemin correct vers les tests unitaires de votre application Python. Vous pouvez également personnaliser d'autres options de configuration de pytest selon vos besoins.
    4- Nom de l'image Docker et version : Dans le fichier Dockerfile, vous pouvez modifier le nom de l'image Docker en mettant à jour la ligne FROM python:3.9 avec l'image et la version souhaitées.
    5- Chemin et contexte du build de l'image Docker : Dans le fichier de pipeline (Jenkinsfile, .gitlab-ci.yml ou .github/workflows/main.yml), assurez-vous de spécifier le chemin correct vers le répertoire contenant le Dockerfile et les fichiers nécessaires pour la construction de l'image Docker. Cela peut être personnalisé en modifiant les paramètres context et dockerfile dans la section de construction de l'image.
    6- Identifiant de connexion pour le hub Docker : Dans le fichier de pipeline (Jenkinsfile, .gitlab-ci.yml ou .github/workflows/main.yml), vous devez spécifier l'identifiant de connexion pour le Docker Hub. Assurez-vous de mettre à jour cet identifiant avec le vôtre.

Assurez-vous de sauvegarder et de valider toutes les modifications apportées aux fichiers avant d'exécuter le pipeline d'intégration continue.

Ceci conclut la documentation pour la mise en place d'une chaîne d'intégration continue pour les applications Python. Suivez les instructions fournies pour configurer et exécuter votre pipeline d'intégration continue avec succès. Si vous rencontrez des problèmes ou avez des questions, n'hésitez pas à demander de l'aide à l'équipe DevOps ou à consulter la documentation supplémentaire appropriée pour les outils spécifiques utilisés (Jenkins, GitLab CI, GitHub Actions, etc.).
