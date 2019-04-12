# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:34:58 2019

@author: Villebon 29
"""

fichier = open("message3.txt","r")
message = fichier.read()

def decaler_message_cesar(message_chiffre, cle):
  """
  Cette fonction prends en argument un message chiffré et une clé à lui appliquer, puis incrémente chaque caractere du message par la clé. Elle retourne le message ainsi déchiffré.
  """
  message_dechiffre = []
  for caractere in message_chiffre:
    #print(caractere)
    numero_caractere_chiffre = ord(caractere)
    numero_caractere_dechiffre = (numero_caractere_chiffre + cle) % 255 # 255 donne rpar arthur car probleme
    caractere_dechiffre = chr(numero_caractere_dechiffre)
    message_dechiffre.append(caractere_dechiffre)
  return "".join(message_dechiffre) #liste en chaine caractere, pas de séparateur

def verifier_message(message_dechiffre:str) -> bool:
  return message_dechiffre.endswith("Joël")

DEBUT_RECHERCHE_CLE = -50
FIN_RECHERCHE_CLE = 50

print("Début recherche")
for cle in range(DEBUT_RECHERCHE_CLE, FIN_RECHERCHE_CLE + 1):
  message_dechiffre = decaler_message_cesar(message, cle)
  if verifier_message(message_dechiffre):
    print("TROUVE!!!")
    print(f"Le message à été correctement déchiffré avec la clé {cle}: Il contient {message_dechiffre}")
    break
else:
  print("probleme")

#print(verifier_message(decaler_message_cesar(message, -6)))