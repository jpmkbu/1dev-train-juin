#imports
import textwrap
import calendrier

#variable demandé
mois=int(input("Un mois s'il vous plait :"))
annee=int(input("Une année s'il vous plait :"))
#affichage du calendrier
calendrier.afficher_titre(mois,annee)
calendrier.afficher_entete()
#décalage des jours et allignement
decalage=calendrier.numero_jour(1,mois,annee)
jours=textwrap.fill(calendrier.suite_numeros_jours(mois,annee),width=26)
affiche=" "*(4*decalage)+jours#      4 équivaut au nombre de caractère dans entête : "Lu--Ma--Me--Je--Ve--Sa--Di--"
print(textwrap.fill(affiche,width=26))







