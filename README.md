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

## Auteur
El hadji Médoune Diallo, étudiant en licence d'informatique à Sup de Co
