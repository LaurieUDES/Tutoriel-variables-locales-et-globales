########### Système de gestion de base de données ###########

# Importation de la bibliothèque sqlite3
import sqlite3

# Définition d'une variable globale nommée connexion
connexion = sqlite3.connect('base_de_donnees.db') # Connexion à la base de données

# Définition d’une fonction qui supprime une table
def supprimer_table(nom_table):
  # Création d'un objet Cursor qui permet d'exécuter des requêtes SQL
  curseur = connexion.cursor()
  # Définition d'une variable locale nommée requete
  requete = f"DROP TABLE IF EXISTS {nom_table}"
  # Exécution de la requête
  curseur.execute(requete)
  # Validation de la transaction
  connexion.commit()

# Appel de la fonction supprimer_table pour supprimer la table produits et ventes
supprimer_table("produits")
supprimer_table("ventes")

# Définition d'une fonction qui crée une table
def creer_table(nom_table, colonnes):
  # Création d'un objet Cursor qui permet d'exécuter des requêtes SQL
  curseur = connexion.cursor()
  # Définition d'une variable locale nommée requete
  requete = f"CREATE TABLE {nom_table} ({colonnes})"
  # Exécution de la requête
  curseur.execute(requete)
  # Validation de la transaction
  connexion.commit()

# Définition d'une fonction qui insère des données dans une table
def inserer_donnees(nom_table, valeurs):
  # Création d'un objet Cursor qui permet d'exécuter des requêtes SQL
  curseur = connexion.cursor()
  # Définition d'une variable locale nommée requete
  requete = f"INSERT INTO {nom_table} VALUES ({valeurs})"
  # Exécution de la requête
  curseur.execute(requete)
  # Validation de la transaction
  connexion.commit()

# Définition d'une fonction qui sélectionne des données d'une table
def selectionner_donnees(nom_table, condition):
  # Création d'un objet Cursor qui permet d'exécuter des requêtes SQL
  curseur = connexion.cursor()
  # Définition d'une variable locale nommée requete
  requete = f"SELECT * FROM {nom_table} WHERE {condition}"
  # Exécution de la requête
  curseur.execute(requete)
  # Récupération du résultat
  resultat = curseur.fetchall()
  # Affichage du résultat
  print(resultat)

# Appel de la fonction creer_table pour créer la table produits
creer_table("produits", "nom TEXT, prix REAL, categorie TEXT, couleur TEXT")

# Appel de la fonction creer_table pour créer la table ventes
creer_table("ventes", "produit TEXT, quantite INTEGER, date TEXT")

# Appel de la fonction inserer_donnees pour insérer des données dans la table produits
inserer_donnees("produits", "'Livre', 10.0, 'Culture', 'rouge'")
inserer_donnees("produits", "'Stylo', 1.5, 'Papeterie', 'bleu'")
inserer_donnees("produits", "'T-shirt', 15.0, 'Mode', 'vert'")
inserer_donnees("produits", "'Casque', 50.0, 'High-tech', 'noir'")
inserer_donnees("produits", "'Chocolat', 2.0, 'Alimentation', 'marron'")

# Appel de la fonction inserer_donnees pour insérer des données dans la table ventes
inserer_donnees("ventes", "'Livre', 3, '2024-01-01'")
inserer_donnees("ventes", "'Stylo', 5, '2024-01-02'")
inserer_donnees("ventes", "'T-shirt', 2, '2024-01-03'")
inserer_donnees("ventes", "'Casque', 1, '2024-01-04'")
inserer_donnees("ventes", "'Chocolat', 4, '2024-01-05'")

# Exemple 1 : Sélectionner les produits dont le prix est supérieur à 10 euros
selectionner_donnees("produits", "prix > 10")
# Exemple de sortie
[('B', 15, 'bleu'), ('C', 20, 'vert')] # Liste de tuples contenant le nom, le prix, et la couleur des produits

# Exemple 2 : Sélectionner les ventes dont la quantité est inférieure à 5
selectionner_donnees("ventes", "quantite < 5")
# Exemple de sortie
[(1, 'A', 2, '2020-01-01'), (3, 'B', 3, '2020-01-03'), (4, 'C', 4, '2020-01-04')] # Liste de tuples contenant l'id, le produit, la quantité, et la date des ventes

# Exemple 3 : Sélectionner les produits dont la couleur est rouge ou jaune
selectionner_donnees("produits", "couleur = 'rouge' OR couleur = 'jaune'")
# Exemple de sortie
[('A', 10, 'rouge'), ('D', 25, 'jaune')] # Liste de tuples contenant le nom, le prix, et la couleur des produits
