########### Code démontrant l’utilisation du mot-clé global pour accéder à une variable globale. ###########

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