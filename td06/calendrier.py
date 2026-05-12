#EXO 1
def nom_du_mois(index):#        Liste des mois de l'années et retour de cette valeur en nombre.
    mois=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Nomvembre","Decembre"]
    return mois[index-1]

#EXO 2&3
def afficher_titre(mois,annee):#        Affichage "graphique" du calendrier + calcul du centrage du titre ou nombre espace=(L(total)-l(texte))/2
    espace=int((26-(len(nom_du_mois(mois))+4))/2)
    print("="*26)
    print(" "*espace,nom_du_mois(mois),annee)
    print("="*26)

#EXO 4
def afficher_entete():
    print("Lu  Ma  Me  Je  Ve  Sa  Di  ")
    print("-"*26)

#EXO 5
def est_bissextiles(annee):#        Calcul de si année bissextile ou non
    return (annee%4==0 and annee%100!=0) or (annee%400==0)

#EXO 6
def suite_numeros_jours(mois,annee):#               Calcul du nombres de jours par mois en fonction de fevrier ET bissextile ou non
    jours_mois="01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  "
    if mois==2:
        if est_bissextiles(annee):
            return jours_mois[0:116]
        else:
            return jours_mois[0:112]
    elif mois in [4,6,9,11]:
        return jours_mois[0:120]
    else:
        return jours_mois

#EXO 7
def numero_jour(jour,mois,annee):#      congruence de Zeller -> h=(q + (13*(m+1)/5) + K + (K/4) + (J/4) + 5J + 5) % 7
    if mois <=2:
        mois+=12
        annee-=1
    q=jour
    m=mois
    K=annee%100
    J=annee//100
    h=(q+((13*(m+1))//5)+K+(K//4)+(J//4)+5*J+5)%7
    return h

