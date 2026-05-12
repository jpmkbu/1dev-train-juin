import random

def hasard(a,b):
    return random.randint(a,b)

def tirer_carte():
    les_valeurs=[2,3,4,5,6,7,8,9,10,"Valet","Dame","Roi","As"]
    nb_valeur=len(les_valeurs)
    les_couleurs=["Pique","Trèfle","Carreau","Coeur"]
    nb_couleurs=len(les_couleurs)
    tirage_val = les_valeurs[hasard(0, nb_valeur-1)]
    tirage_couleur = les_couleurs[hasard(0, nb_couleurs-1)]
    return [tirage_val, tirage_couleur]






