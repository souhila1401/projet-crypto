# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:34:58 2019

@author: Villebon 29
"""

fichier = open("message5.txt","r")
message = fichier.read()

def decaler_lettre_cesar(caractere:str, cle:int) -> str:
  numero_caractere_chiffre = ord(caractere)
  numero_caractere_dechiffre = (numero_caractere_chiffre + cle) % 255
  caractere_dechiffre = chr(numero_caractere_dechiffre)
  return caractere_dechiffre

def decaler_message_cesar(message_chiffre:str , cles:list) -> str:
  """
  Cette fonction prends en argument un message chiffré et une clé à lui appliquer, puis incrémente chaque caractere du message par la clé. Elle retourne le message ainsi déchiffré.
  """
  message_dechiffre = []
  for position, caractere in enumerate(message_chiffre):
    #print(caractere)
    
    cle_choisie = cles[position%len(cles)]
    message_dechiffre.append(decaler_lettre_cesar(caractere, cle_choisie))
  return "".join(message_dechiffre) #liste en chaine caractere, pas de séparateur

def verifier_message(message_dechiffre:str) -> bool:
  return message_dechiffre.endswith("Joël")

DEBUT_RECHERCHE_CLE = -10
FIN_RECHERCHE_CLE = 0

print("Début recherche")
for cle1 in range(DEBUT_RECHERCHE_CLE, FIN_RECHERCHE_CLE + 1):
  for cle2 in range(DEBUT_RECHERCHE_CLE, FIN_RECHERCHE_CLE + 1):
    for cle3 in range(DEBUT_RECHERCHE_CLE, FIN_RECHERCHE_CLE + 1):
      cles = [cle1, cle2, cle3]
      message_dechiffre = decaler_message_cesar(message, cles)
      if verifier_message(message_dechiffre):
        print("TROUVE!!!")
        print(f"Le message à été correctement déchiffré avec la clé {cles}: Il contient {message_dechiffre}")
        break

#print(verifier_message(decaler_message_cesar(message, -6)))