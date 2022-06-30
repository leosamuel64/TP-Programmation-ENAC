def affiche(p):
    print(' -'+('---'*len(p[0]))+'- ')
    for ligne in p:
        res="|  "
        for char in ligne:
            res+=str(char)+'  '
        print(res+'|')
    print(' -'+('---'*len(p[0]))+'- ')
        

def remplissage(n,affichage=True):
    t=[[-1 for _ in range(n)] for _ in range(n)]
    ligne=-1
    colonne=n//2 
    passe=0
    
    for k in range(1,(n**2)+1):
        if (passe%n)==0:
            ligne+=1
        else:
            ligne-=1
            colonne+=1
        
        if ligne==-1:
            ligne=n-1
        if colonne==n:
            colonne=0
        t[ligne][colonne]=k
        passe+=1
        
    if affichage:
        affiche(t)
    return t
        

def somme_ligne(t,i):
    return sum(t[i])

def somme_colonne(t,i):
    somme=0
    for ligne in t:
        somme += ligne[i]
    return somme

def somme_diago(t,i):
    somme=0
    if i==0:
        for j in range(len(t)):
            somme+=t[j][j]
    else:
        for j in range(len(t)):
            somme+=t[len(t)-j-1][j]
    return somme

def verif(t):
    somme=somme_ligne(t,0)
    res=True
    for i in range(len(t)):
        res= res and (somme==somme_ligne(t,i))
        res= res and (somme==somme_colonne(t,i))
    for i in range(2):
        res= res and (somme==somme_diago(t,i))
        
    return res

for i in range(3,20,2):
    print(i,verif(remplissage(i,affichage=False)))

        