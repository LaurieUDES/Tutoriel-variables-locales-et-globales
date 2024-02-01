########### Code démontrant l’utilisation d’une variable globale. ###########

# Une variable globale nommée ventes_etats_unis
ventes_etats_unis = 200

# Définition d'une fonction qui affiche la valeur de ventes_etats_unis
def afficher_ventes_etats_unis():
  # Utilisation de la variable globale ventes_etats_unis
  print(ventes_etats_unis)

afficher_ventes_etats_unis() # Affiche 200
print(ventes_etats_unis) # Affiche 200