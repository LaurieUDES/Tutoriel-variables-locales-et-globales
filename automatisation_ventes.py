########### Exemple d’automatisation de ventes ###########

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
  message = f"Bonjour {vendeur['nom']},\nFélicitations pour vos ventes du mois dernier. Vous avez gagné {vendeur['commissions']} euros de commissions.\nContinuez comme ça et vous atteindrez bientôt vos objectifs.\nCordialement,\nL'équipe GTA431."
  # On appelle la fonction globale qui envoie le courriel
  envoyer_courriel(vendeur['nom'], message)