import simui as s

def afficherVol(L):
    print('----- Début des vols -----')
    i=0
    for (imat,src,dest) in L:
        print('['+str(i)+']',imat,src,dest)
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
    
    