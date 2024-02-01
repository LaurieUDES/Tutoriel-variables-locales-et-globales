########### Code démontrant l’ombrage d’une variable globale par une variable locale du même nom ###########

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