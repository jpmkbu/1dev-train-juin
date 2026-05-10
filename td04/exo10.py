a=int(input("veuillez entrer un 1er nombre:"))
b=int(input("veuillez entrer un 2e nombre:"))
c=int(input("veuillez entrer un 3e nombre:"))
d=int(input("veuillez entrer un 4e nombre:"))
#b et d ne peuvent être égales à 0.
if b== 0 or d==0:
    print("Les dénominateurs ne peuvent être égales à 0!")
#Déterminer a/b = c/d
elif a*d==c*b:
    print("True")  
else:
    print("False")      


# #Egalité de fractions
# #
# a=int(input("Veuillez introduire le premier nombre:"))
# b=int(input("Veuillez introduire le deuxième nombre:"))
# c=int(input("Veuillez introduire le troisième nombre:"))
# d=int(input("Veuillez introduire le quatrième nombre:"))
# #b et d ne peuvent être égales à 0.
# if b==0 or d==0:
#     print("Les dénominateurs ne peuvent être égales à 0!")
# #Déterminer a/b = c/d
# elif a*d==c*b:
#     print("True")
# else:
#     print("False")
