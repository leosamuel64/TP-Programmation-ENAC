from time import time
from matplotlib import pyplot as plt

def est_premier(n):   # O(n)
    i=2
    premier=True
    while premier and i <= n**0.5:
        if n%i==0:
            premier=False
        else:
            i+=1
    return premier and n>1

# print(est_premier(25))

def est_premier_boucle(n):
    for i in range(n+1):
        nb = int(input("Nombre :"))
        print(est_premier(nb))

# est_premier_boucle(10)

def nombre_premier_avant(n):    # O(n²)
    res = []
    for i in range(n+1):       
        if est_premier(i):      
            res.append(i)
    return res

# print(nombre_premier_avant(100000))

def n_nb_premier(i):
    count = 0
    n=25
    while count<n:
        if est_premier(i):
            count+=1
            print(i)
        i+=1

# n_nb_premier(110)

def liste_erathosthene(n):
    L=[True for _ in range(n)]

    L[0]=False
    L[1]=False
    for i in range(2,n):
        if L[i]:
            for j in range(i*i, n,i):
                L[j]=False
    return L

def liste_erathosthene2(n):                     # O(nlog(log(n)))
    L=[True for _ in range(n)]

    for i in range(3,n):
        if L[i]%2==0:
            L[i]= False
    
    L[0]=False
    L[1]=False

    for i in range(2,n):                        
        if L[i]:
            for j in range(i*i, n,i):           
                L[j]=False
    return L


def liste_erathosthene3(n):                     # O(nlog(log(n)))
    L=[True for _ in range(n)]

    for i in range(3,n):
        if L[i]%2==0 or L[i]%3==0:
            L[i]= False
    
    L[0]=False
    L[1]=False

    for i in range(2,n):                        
        if L[i]:
            for j in range(i*i, n,i):           
                L[j]=False
    return L

def liste_erathosthene5(n):                     # O(nlog(log(n)))
    L=[True for _ in range(n)]

    for i in range(3,n):
        if L[i]%2==0 or L[i]%3==0 or L[i]%5==0:
            L[i]= False
    
    L[0]=False
    L[1]=False

    for i in range(2,n):                        
        if L[i]:
            for j in range(i*i, n,i):           
                L[j]=False
    return L

def erathosthene(n):                            # O(nlog(log(n)))
    l = liste_erathosthene(n)
    return [i for i in range(len(l)) if l[i]]

def erathosthene2(n):                           # O(nlog(log(n)))
    l = liste_erathosthene2(n)
    return [i for i in range(len(l)) if l[i]]

def erathosthene3(n):                           # O(nlog(log(n)))
    l = liste_erathosthene3(n)
    return [i for i in range(len(l)) if l[i]]

def erathosthene5(n):                           # O(nlog(log(n)))
    l = liste_erathosthene5(n)
    return [i for i in range(len(l)) if l[i]]


def compare(liste_fonctions, liste_noms, n,pas):
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


compare(    [erathosthene,erathosthene2,erathosthene3,erathosthene5],
            ["Erathosthene", "Erathosthene Opti Paires", "Erathosthene Opti Paires & Triples","Erathosthene Opti Paires, Triples & Quintuples"],
            100000,
            1000
        )
