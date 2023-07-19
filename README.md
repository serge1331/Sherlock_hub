# Sherlock_hub
sherlock

## Lancement de l'api

Emplacement: /api/app

### Créer un environnement python

python3 -m venv nom_environnement

### Installer les dépendances 

python3 install -r requirements.txt

### Lancer le projet 

uvicorn src.main:app --reload 


## Structure de l'API

/api
    /app
        /src
            /collect
                __init__.py
                collect.py

            /Data_collectors
                __init__.py
                pygooglenews_collector.py

            /templates

            /test

            __init__.py
            analyse_sentiments.py
            Dataset_generator.py
            main.py
            .env
            .gitignore
        
README.md

## Explication de la structure

### Collecte des données

La collecte des données est gérée par le package **Data_collectors**.Chaque module de ce package est collecte des données à une source unique. Dans le cas du module **pygooglenews_collector** utilisé dans ce projet, la source de données est **Google News**. Je décrirai plus bas dans cette documentation le structure à respecter pour que les données collectées par le module soientt pris en charge par l'application.

### Génération du dataframe 

Le dataframe est généré au niveau de la fonction **generator** du module **Dataset_generator**.

### Analyse des opinions

L'analyse des opinions est géré dans le module **sentiment_analyzer** dans dans la fonction **sentiment** et les resultats sont retournés dans la fonction **result** 


## Structure des modules de collecte de données

Les modules de collecte de données sont des plugins qui peuvent être ajoutés à l'application afin d'augmenter le nombre de sources disponibles. Ces modules nécessitent donc un formatage précis pour être pris en compte.

### Structure

La structure est relativement simple. Un module de colecte doit obligatoirement disposer d'une fonction ***collect*** qui retourne les données collectées sous forme d'une liste de dictionnaires. Chaque dictionnaire doit contenir nécessairement une clé ***opinion*** qui représente l'avis (déjà nettoyer) à analyser.


