########### Exemple d’une analyse de ventes ###########

# On importe les modules pandas et statistics
import pandas as pd
import statistics as st

# On définit une variable globale pour le nom de la colonne
colonne = "ventes"

# On lit le fichier CSV avec pandas et on stocke le résultat dans une variable df
df = pd.read_csv("ventes.csv")

# On extrait la colonne de ventes avec pandas et on la convertit en une liste
ventes = df[colonne].tolist()

# On calcule la moyenne, la médiane et l'écart-type des ventes avec statistics et on stocke les résultats dans des variables locales
moyenne = st.mean(ventes)
mediane = st.median(ventes)
ecart_type = st.stdev(ventes)

# On affiche les résultats avec des chaînes de caractères formatées
print(f"La moyenne des ventes est {moyenne:.2f} euros")
print(f"La médiane des ventes est {mediane:.2f} euros")
print(f"L'écart-type des ventes est {ecart_type:.2f} euros")