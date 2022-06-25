from time import time
from matplotlib import pyplot as plt

def compare_fonction(liste_fonctions, liste_noms, n,pas):
    """
    Compare en temps une liste de fonctions et trace le résulat
    """
    liste_coord=[([],[],i) for i in range(len(liste_fonctions))]
    for k in range(10,n,pas):
        print(k)
        for i in range(len(liste_fonctions)):
            deb=time()
            liste_fonctions[i](k)
            t=time()-deb

            liste_coord[i][0].append(k)
            liste_coord[i][1].append(t)
    
    for (x,y,i) in liste_coord:
        plt.scatter(x,y,label=liste_noms[i])

    plt.xlabel('Taille')
    plt.ylabel('Temps (s)')
    plt.legend()
    plt.show()