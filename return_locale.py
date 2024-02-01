########### Code démontrant les limites de l’utilisation d’une variable locale. ###########

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