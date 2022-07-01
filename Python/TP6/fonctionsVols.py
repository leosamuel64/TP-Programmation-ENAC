import simui as s

def afficherVol(L,dico):
    print('----- Début des vols -----')
    i=0
    for (imat,src,dest) in L:
        print('['+str(i)+']',imat,src,dest,int(distance_terrain(src,dest,dico)),'km')
        i+=1
    print('----- Fin des vols -----')
    _=input('Appuyez sur [ENTER] pour continuer')
        
def ajoutVol(L):
    print("----- Début de l'ajout -----")
    imat=input("Immatriculation de l'appareil : ")
    src=input("Aérodrome de départ (OACI) : ")
    dest=input("Aérodrome d'arrivé (OACI) : ")
    L.append((imat.upper(),src.upper(),dest.upper()))
    print("----- Fin de l'ajout -----")
    
def supprimeVol(L):
    indice=input("Indice du vol à supprimer : ")
    L.pop(int(indice))
    
    
def supprimeVol2(L):
    res=[]
    for (imat,src,dest) in L:
        res.append(imat+' '+src+' '+dest)
    indice = s.menu(res)
    L.pop(int(indice))
    
def charger(chemin):
    vols=[]
    file=open(chemin,'r') 
    for l in file:
        imat,src,dest=l.split(' ')
        vols.append((imat,src,dest.strip()))
    file.close() 
    return vols

def sauver(chemin,vols):
    file=open(chemin,'w')
    for (imat,src,dest) in vols:
        file.write(imat+' '+src+' '+dest+'\r')
    file.close()
    
def charge_terrain(chemin):
    file=open(chemin,'r')
    res={}
    for ligne in file:
        temp=[]
        
        deg=ligne.split(' ')
        for i in deg:
            if i!='':
                temp.append(i)
        l=[temp[i] for i in range(3)]
        icao, x, y = l
        res[icao]=(int(x),int(y))
    return res
        
def distance(X,Y):
    return ((X[0]-Y[0])**2 + (X[1]-Y[1])**2)**(1/2)



def distance_terrain(a,b,dico):
    return distance(dico[a],dico[b])
        
    
        
