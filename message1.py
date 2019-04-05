# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#fichier= open("C:\Users\Villebon 29\Desktop\Cryptographie","r");
#fichier.open();


message="abcdefghijkl";

nbrcarac = len(message)#longueur du message a décrypter
key = 3 # key donné par moi
nbrligne = key  # nombre de colonne est égale a la clé 
nbrcolonne= nbrcarac / key # dans mon tableau
decrypter= ['']*float.nbrcolonne #TABLEAU VIDE


ligne = 0 # initialisé pour le tableau et lui dire ou on commence à la ligne 0
colonne = 0

for i in message :
    #  equivaut decrypter= decrypter + i
    decrypter[colonne] += i 
    colonne +=1

print(decrypter)


#for i in range (4):
#    for j in range(i,1,4):
#        j=j+1
#        message=i
#print(message,i)

    