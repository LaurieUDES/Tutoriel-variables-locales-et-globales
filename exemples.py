##################################################################################################
# Exemple 1: Code démontrant l’utilisation d’une variable locale.
def calculer_ventes_totales():
  # Une variable locale nommée ventes_totales
  ventes_totales = ventes_france + ventes_canada + ventes_etats_unis
  # On renvoie la valeur de la variable locale ventes_totales
  return ventes_totales

# On définit des variables globales pour les ventes de chaque pays
ventes_france = 100
ventes_canada = 150
ventes_etats_unis = 200

# On appelle la fonction calculer_ventes_totales et on stocke sa valeur de retour dans une variable resultat
resultat = calculer_ventes_totales()
# On affiche la valeur de la variable resultat
print(resultat) # Affiche 450

##################################################################################################
# Exemple 2: Code démontrant l’utilisation du mot-clé global pour accéder à une variable globale.
# Une variable globale nommée ventes_france
ventes_france = 100

def augmenter_ventes_france():
  # On utilise le mot-clé global pour accéder à la variable globale ventes_france
  global ventes_france
  # On modifie la valeur de la variable globale ventes_france
  ventes_france = ventes_france + 10
  print(ventes_france) # Affiche 110

# On appelle la fonction augmenter_ventes_france
augmenter_ventes_france()
# On vérifie la valeur de la variable globale ventes_france après l'appel de la fonction
print(ventes_france) # Affiche 110

##################################################################################################
# Exemple 3: Code illustrant les implications de la portée des variables dans la manipulation de données.
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

##################################################################################################
# Exemple 4: Code démontrant l’utilisation d’une variable globale.
# Une variable globale nommée ventes_etats_unis
ventes_etats_unis = 200

# Définition d'une fonction qui affiche la valeur de ventes_etats_unis
def afficher_ventes_etats_unis():
  # Utilisation de la variable globale ventes_etats_unis
  print(ventes_etats_unis)

afficher_ventes_etats_unis() # Affiche 200
print(ventes_etats_unis) # Affiche 200

##################################################################################################
# Exemple 5: Code démontrant l’utilisation d’une variable locale.
# Définition d'une fonction qui calcule le pourcentage des ventes d'un produit par rapport au total
def calculer_pourcentage(ventes_produit):
  # Définition d'une variable locale nommée pourcentage
  pourcentage = (ventes_produit / ventes_totales) * 100
  # Retour de la valeur de pourcentage
  return pourcentage

# On définit des variables globales pour les ventes de chaque produit et le total
ventes_a = 100
ventes_b = 150
ventes_c = 200
ventes_totales = 450

# Appel de la fonction calculer_pourcentage avec l'argument ventes_a
pourcentage_a = calculer_pourcentage(ventes_a)
print(pourcentage_a) # Affiche 22.22
print(pourcentage) # Erreur : pourcentage n'est pas défini


##################################################################################################
# Exemple 6: Code démontrant l’ombrage d’une variable globale par une variable locale du même nom.
# Une variable globale nommée ventes_canada
ventes_canada = 150

def modifier_ventes_canada():
  # Une variable locale nommée ventes_canada
  ventes_canada = 160
  print(ventes_canada) # Affiche 160

# Appel de la fonction modifier_ventes_canada
modifier_ventes_canada()
# Affichage de la valeur de ventes_canada
print(ventes_canada) # Affiche 150

##################################################################################################
# Exemple 7: Exemple d’une analyse de ventes
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

##################################################################################################
# Exemple 8: Exemple de visualisation de ventes
# On importe la bibliothèque matplotlib
import matplotlib.pyplot as plt

# On crée une liste de ventes aléatoires
ventes = [200, 400, 400, 500, 600, 700, 700, 700, 800, 800, 800, 1200, 1300]

# On définit une variable globale pour la couleur des barres
couleur = "orange"

# On crée un objet figure avec la fonction plt.subplots()
fig, ax = plt.subplots()

# On crée un histogramme avec la fonction plt.hist()
ax.hist(ventes, color=couleur, edgecolor="black")

# On ajoute un titre et des étiquettes aux axes
ax.set_title("Exemple d'histogramme des ventes avec matplotlib")
ax.set_xlabel("Ventes (en euros)")
ax.set_ylabel("Fréquences")

# On affiche la figure
plt.show()

##################################################################################################
# Exemple 9: Exemple d’automatisation de ventes
# Une variable globale qui contient la fonction qui envoie le courriel
def envoyer_courriel(destinataire, message):
  # Ici, vous pouvez utiliser une bibliothèque comme smtplib pour envoyer le courriel
  print(f"Envoi du courriel à {destinataire} avec le message: {message}")

# Une liste de vendeurs avec leurs commissions
vendeurs = [
  {"nom": "Alice", "commissions": 120},
  {"nom": "Bob", "commissions": 240},
  {"nom": "Charlie", "commissions": 180}
]

# Une boucle qui parcourt les vendeurs et crée un message personnalisé pour chacun
for vendeur in vendeurs:
  # Une variable locale qui stocke le message à envoyer
  message = f"Bonjour {vendeur['nom']},\nFélicitations pour vos ventes du mois dernier. Vous avez gagné {vendeur['commissions']} euros de commissions.\nContinuez comme ça et vous atteindrez bientôt vos objectifs.\nCordialement,\nL'équipe Bing."
  # On appelle la fonction globale qui envoie le courriel
  envoyer_courriel(vendeur['nom'], message)