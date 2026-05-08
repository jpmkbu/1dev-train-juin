n1=float(input("veuillez entre un 1er côte:"))
n2=float(input("veuillez entre un 2e côte:"))
n3=float(input("veuillez entre un 3e côte:"))

if n1==n2==n3:
    print("equi")
if n1==n2 or n1==n3 or n2==n3:
    print("iso")
else:
    print("quelconque")    




