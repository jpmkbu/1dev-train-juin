import random

3  # Retourne un nombre aléatoire entre a et b (appelée par la fonction lettres())


def hasard(a, b):

    return random.randint(a, b)


# Tire 3 lettres de l'alphabet au hasard (répétitions possibles) et les renvoie
def lettres():
    alphabet = "abcdefghijklmnopqrsyuvwxyz"

    nb_lettres = len(alphabet)
    lettre1 = alphabet[hasard(0, nb_lettres - 1)]
    lettre2 = alphabet[hasard(0, nb_lettres - 1)]
    lettre3 = alphabet[hasard(0, nb_lettres - 1)]
    return sorted([lettre1, lettre2, lettre3])
