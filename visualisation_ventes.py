########### Exemple de visualisation de ventes ###########

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