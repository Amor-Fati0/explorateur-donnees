# Explorateur de données mondiales

Application web en Python pour comparer des indicateurs de développement entre pays (population, PIB par habitant, espérance de vie, accès à internet), à partir de l'API de la Banque mondiale.

## Fonctionnalités
- Choix de plusieurs pays parmi tous ceux de la Banque mondiale
- Choix de l'indicateur
- Graphique interactif (survol, zoom) et tableau des données
- Nouvel essai automatique si l'API ne répond pas

## Technologies
Python, Streamlit, pandas, requests, Plotly

## Lancer le projet

    pip install -r requirements.txt
    python -m streamlit run app.py

## Ce que j'ai appris
- Appeler une API avec requests et lire du JSON
- Nettoyer et organiser des données avec pandas
- Gérer les erreurs avec try / except
- Créer des graphiques interactifs avec Plotly
- Construire une interface web avec Streamlit

## Auteur
Diallo Adu, étudiant en licence d'informatique à Sup de Co