# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:28:09 2019

@author: Villebon 29
"""

"""
lignes commune à tous les messages à déchiffrer , elle permet d'ouvrir les message et de les lire 

"""

fichier = open("message2.txt","r")
message = fichier.read()


def decaler_message_cesar(message_chiffre, cle):
  """
  Cette fonction prends en argument un message chiffré et une clé à lui appliquer, puis incrémente chaque caractere du message par la clé. Elle retourne le message ainsi déchiffré.
  """
  message_dechiffre = [] # tABLEAU VIDE POUR METTRE LE MESSAGE DECHIFFREE
  for caractere in message_chiffre:
    #print(caractere)
    numero_caractere_chiffre = ord(caractere) #Renvoie le nombre entier représentant le code Unicode du caractère représenté par la chaîne donnée
    numero_caractere_dechiffre = (numero_caractere_chiffre + cle) % 255 # 255 donne rpar arthur car probleme
    caractere_dechiffre = chr(numero_caractere_dechiffre) #envoie la chaîne représentant un caractère dont le code de caractère Unicode est le nombre entier i.
    message_dechiffre.append(caractere_dechiffre)
  return "".join(message_dechiffre) #liste en chaine caractere, pas de séparateur

def verifier_message(message_dechiffre):
  """
Cette fonction verifie si à la fin du message dechiffrer, on retrouve un mot commun au messahe
elle retourne alors joel 
  """
  return message_dechiffre.endswith("Joël")

DEBUT_RECHERCHE_CLE = -50 #INTERVALLE DE RECHERCHE POUR CHERCHER LA CLE
FIN_RECHERCHE_CLE = 50
print("Début recherche")


for cle in range(DEBUT_RECHERCHE_CLE, FIN_RECHERCHE_CLE + 1): # boucle qui permet de retrouve la cle 
  message_dechiffre = decaler_message_cesar(message, cle)
  if verifier_message(message_dechiffre):# si le message st trouveée 
    print("TROUVE!!!")
    print(f"Le message à été correctement déchiffré avec la clé numéro {cle}: Il contient {message_dechiffre}")
    break
else:
  print("problème")


