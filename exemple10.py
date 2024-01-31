# Importation de la bibliothèque kafka-python
import kafka

# Définition d'une variable globale nommée donnees_temps_reel
donnees_temps_reel = []

# Définition d'une fonction qui consomme les données du flux kafka
def consommer_donnees():
  # Création d'un objet Consumer qui se connecte au serveur kafka
  consommateur = kafka.Consumer('flux_donnees', bootstrap_servers='localhost:9092')
  # Boucle infinie qui lit les messages du flux
  for message in consommateur:
    # Extraction des données du message
    donnees = message.value
    # Ajout des données à la variable globale donnees_temps_reel
    donnees_temps_reel.append(donnees)
    # Appel d'une fonction qui analyse les données
    analyser_donnees(donnees)

# Définition d'une fonction qui analyse les données
def analyser_donnees(donnees):
  # Définition d'une variable locale nommée resultat
  resultat = {}
  # Calcul de quelques statistiques sur les données
  resultat['moyenne'] = sum(donnees) / len(donnees)
  resultat['minimum'] = min(donnees)
  resultat['maximum'] = max(donnees)
  # Affichage du résultat
  print(resultat)

# Lancement du code
consommer_donnees()

# Exemple de sortie
{'moyenne': 0.5, 'minimum': 0, 'maximum': 1} # Résultat de l'analyse du premier message
{'moyenne': 0.4, 'minimum': 0, 'maximum': 1} # Résultat de l'analyse du deuxième message
{'moyenne': 0.6, 'minimum': 0, 'maximum': 1} # Résultat de l'analyse du troisième message

