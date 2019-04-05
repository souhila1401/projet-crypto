# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:57:00 2019

@author: Villebon 29
"""
def compter_occurences(caractere, chaine):
    nbr_car=0 # initiation du nombre d'occurrence par 0
    for caractere in chaine: # parcourt de la chaine 
        if caractere==chaine:
            nbr_car+=1; # incrémentation de la variable nbr_char à chaque rencontre du caractère c
    return nbr_car

print(compter_occurences("jifezifubufbziubzeuiebuibfz","j"))

def compter_mot(chaine,mot): 
     nbr_mot=0
     for caractere in chaine :
         if nbr_mot == chaine:
             nbr_mot+=1
             return nbr_mot
         else:
             return 0;
print (compter_mot("dkdhkbgerjkgbrjkbrdkd","dkd"))
        
            
            

    
     
     
        
        
        
    