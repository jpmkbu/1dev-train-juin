t=str(input("veuillez entrer un texte:"))
c=t.count(" ") 
if c>1:
    print("contient plus d'un espace")
elif c==1:
    print("contient un espace")
else:
    print("ne contient pas d'espace")    