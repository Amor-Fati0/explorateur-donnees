import requests
import pandas as pd
import streamlit as st
import time
import plotly.express as px


def recuperer_donnees(pays, indicateur, debut=2000, fin=2023):
    """Va chercher un indicateur de la Banque mondiale. Renvoie None si l'API ne répond pas."""
    codes = ";".join(pays)
    url = f"https://api.worldbank.org/v2/country/{codes}/indicator/{indicateur}"
    params = {"format": "json", "per_page": 1000, "date": f"{debut}:{fin}"}

    contenu = None
    for tentative in range(3):
        try:
            reponse = requests.get(url, params=params, timeout=30)
            reponse.raise_for_status()
            contenu = reponse.json()
            break  # ça a marché, on sort de la boucle
        except (requests.exceptions.RequestException, ValueError):
            time.sleep(2)  # on attend 2 secondes avant de réessayer

    if contenu is None:
        return None  # les 3 essais ont échoué

    if len(contenu) < 2 or contenu[1] is None:
        return pd.DataFrame()

    lignes = []
    for element in contenu[1]:
        if element["value"] is not None:
            lignes.append({
                "Pays": element["country"]["value"],
                "Année": int(element["date"]),
                "Valeur": element["value"],
            })
    return pd.DataFrame(lignes)


# st.title("Explorateur de données mondiales")

# df = recuperer_donnees(["SEN", "FRA", "BRA"], "SP.POP.TOTL")
# st.dataframe(df)
@st.cache_data
def recuperer_pays():
    """Renvoie un dictionnaire {nom du pays: code} pour tous les pays."""
    url = "https://api.worldbank.org/v2/country"
    params = {"format": "json", "per_page": 400}

    reponse = requests.get(url, params=params, timeout=20)
    reponse.raise_for_status()
    contenu = reponse.json()

    pays = {}
    for element in contenu[1]:
        if element["region"]["id"] != "NA":  # "NA" = regroupements (Monde, Euro...), pas des pays
            pays[element["name"]] = element["id"]
    return dict(sorted(pays.items()))



st.title("Explorateur de données mondiales")

PAYS = recuperer_pays()
INDICATEURS = {
    "Population totale": "SP.POP.TOTL",
    "PIB par habitant (USD)": "NY.GDP.PCAP.CD",
    "Espérance de vie (années)": "SP.DYN.LE00.IN",
    "Utilisateurs d'internet (%)": "IT.NET.USER.ZS",
}

pays_choisis = st.multiselect(
    "Choisis des pays", list(PAYS.keys()), default=["Senegal", "France"]
)
indicateur_choisi = st.selectbox("Choisis un indicateur", list(INDICATEURS.keys()))

if len(pays_choisis) == 0:
    st.warning("Choisis au moins un pays.")
else:
    codes_pays = [PAYS[nom] for nom in pays_choisis]
    code_indicateur = INDICATEURS[indicateur_choisi]
    df = recuperer_donnees(codes_pays, code_indicateur)

    if df.empty:
        st.info("Aucune donnée trouvée pour cette sélection.")
    else:
        df = df.sort_values(["Pays", "Année"])

        fig = px.line(
            df,
            x="Année",
            y="Valeur",
            color="Pays",
            markers=True,
            title=indicateur_choisi,
        )
        fig.update_layout(yaxis_title=indicateur_choisi, hovermode="x unified")
        st.plotly_chart(fig)

        with st.expander("Voir les données"):
            st.dataframe(df)