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