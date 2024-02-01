########### Code illustrant les implications de la portée des variables dans la manipulation de données. ###########

# Importation de la bibliothèque pandas
import pandas as pd

# Définition d'une variable globale nommée donnees
donnees = pd.read_csv("ventes.csv") # Lecture du fichier CSV contenant les données sur les ventes

# Définition d'une fonction qui calcule le total des ventes par produit
def calculer_total_par_produit():
  # Définition d'une variable locale nommée total
  donnees = donnees.groupby("produit").sum() # Regroupement des données par produit et somme des ventes
  # Retour de la valeur de total
  return donnees

# Appel de la fonction calculer_total_par_produit
resultat = calculer_total_par_produit()

# Affichage du résultat
print(resultat)

# Affichage de la valeur de donnees
print(donnees) # Erreur : référence circulaire