# Exemple 10: Analyse de données en temps réel

import pandas as pd
import numpy as np
import time

# Définition d'une variable globale nommée donnees_temps_reel
donnees_temps_reel = []

# Définition d'une fonction qui génère des données en temps réel
def generer_donnees():
    global donnees_temps_reel
    # Génération d'une valeur aléatoire
    valeur = np.random.random()
    # Ajout de la valeur à la variable globale donnees_temps_reel
    donnees_temps_reel.append(valeur)

# Définition d'une fonction qui analyse les données
def analyser_donnees():
    global donnees_temps_reel
    # Conversion des données en une série pandas
    serie = pd.Series(donnees_temps_reel)
    # Calcul de la moyenne mobile sur les 5 dernières données
    moyenne_mobile = serie.rolling(window=5).mean()
    # Affichage de la moyenne mobile
    print(moyenne_mobile)

# Lancement du code
while True:
    generer_donnees()
    analyser_donnees()
    # Pause de 1 seconde entre chaque génération de données
    time.sleep(1)
