import random

# Retourne un nombre aléatoire entre a et b (appelée par la fonction lettres())
def hasard (a,b):
 return random.randint(a,b)

# Tire une couleur aléatoire et la retourne
def couleurs ():
 les_couleurs = ['rouge', 'vert', 'jaune', 'bleu', 'blanc', 'noir' ]
 nb_couleurs = len(les_couleurs)

 couleur = les_couleurs[hasard(0,nb_couleurs-1)]

 return couleur

print(couleurs())
 



