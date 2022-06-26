from time import time
from matplotlib import pyplot as plt

def moyenne_liste(l):
    somme=0
    for i in l:
        somme+=i
    return somme/len(l)

def compare_fonction(liste_fonctions, liste_noms, liste_objets,repet=1):
    """
    Compare en temps une liste de fonctions et trace le résulat
    - liste_objets : objet à passer en argument des fonctions à comparer
    - repet : nombre de repetition pour chaque objet de la liste
    """
    liste_coord=[([],[],i) for i in range(len(liste_fonctions))]
    
    for k in range(len(liste_objets)):
        for i in range(len(liste_fonctions)):
            for j in range(repet):
                print(k,j)
                deb=time()
                liste_fonctions[i](liste_objets[k])
                t=time()-deb

                liste_coord[i][0].append(k)
                liste_coord[i][1].append(t)
    
    for (x,y,i) in liste_coord:
        plt.scatter(x,y,label=liste_noms[i])
        
    tps_moyen=[moyenne_liste(t) for _,t,_ in liste_coord]
    for k in range(len(liste_coord)):
        print(liste_noms[k],tps_moyen[k])
        

    plt.xlabel('Taille')
    plt.ylabel('Temps (s)')
    plt.legend()
    plt.show()