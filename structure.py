
# Script de création de bibliothèque de JCC en revente
# Le script permet de créer une base de données intégrant des dictionnaires de cartes, de propriétaires, de prix de vente,
# et de taux de commission de revente afin de calculer les bénéfices réalisés et répartir les gains

# Menu de lancement -Structure conditionnelle à choix multiples

import numpy as np
import pandas as pd
import json as js # création du dictionnaire de cartes

with open(~/Dropbox/Perso/Projet_cardshuffle/pool.json, 'r') as pool:
    catalogue = js.load(pool)

def add_card(self, ajouter):
    new_card = str(input("Indiquez le nom de la carte"))
    if new_card in catalogue
        print("La carte existe déjà")
    else:
        donnees_cartes = {"nom_carte":"édition", "nom_carte":"prix", "nom_carte":"propriétaire", "nom_carte":"quantité"}
        nom_carte = bool(input("Validez le nom de la carte"))
        if nom_carte = False
            return
        édition = str(input("Indiquez l'édition de la carte"))
        prix = float(input("Indiquez le prix de la carte"))
        propriétaire = str(input("Indiquez le nom du propriétaire"))
            if propriétaire in seller = True

            else:
                print("Le propriétaire n'est pas dans la base")
        quantité = int(input("Indiquez la quantité de cette carte en vente"))

with open(pool, 'w') as catalogue
    js.dump(donnees_cartes, pool, indent=1)

def remove_card():

def add_seller():
    seller = {"nom_vendeur":"à_vendre", "solde"}

def check_seller():


choix = int(input("Entrez votre choix entre 1 et 4"))
while True
if choix = [1..4] 
    match (choix)

#ajouter une carte
        case 1:
            print("Ajouter une carte")
            add_card()

#retirer une carte
        case 2:
            print("Retirer une carte")
            remove_card()

#ajouter un vendeur
        case 3:
            print("Ajouter un vendeur")
            add_seller()

#consulter un vendeur
        case 4:
            print("Consulter un vendeur")
            check_seller()
else:
    break        