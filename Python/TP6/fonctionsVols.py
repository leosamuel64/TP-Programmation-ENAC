import datetime
import simui as s

V=230

def afficherVol(L,dico):
    print('----- Début des vols -----')
    i=0
    for (date,imat,src,dest) in L:
        distance=distance_terrain(src,dest,dico)
        type_distance=type(distance)
        print('['+str(i)+']',
              imat+' |',
              src+' |',
              dest+' |',
              int(distance) if type_distance==float else 'Code OACI inconnu',
              'km |' if type_distance==float else ' |',
              formate_temps(int(temps_de_vol(V,distance))) if type_distance==float else 'Code OACI inconnu'
              )
        i+=1
    print('----- Fin des vols -----')
    _=input('Appuyez sur [ENTER] pour continuer')
        
def ajoutVol(L):
    print("----- Début de l'ajout -----")
    date=input('Date du vol : JJ/MM/AA ')
    imat=input("Immatriculation de l'appareil : ")
    src=input("Aérodrome de départ (OACI) : ")
    dest=input("Aérodrome d'arrivé (OACI) : ")
    L.append((date,imat.upper(),src.upper(),dest.upper()))
    print("----- Fin de l'ajout -----")
    
def supprimeVol(L):
    indice=input("Indice du vol à supprimer : ")
    L.pop(int(indice))
    
    
def supprimeVol2(L):
    res=[]
    for (date,imat,src,dest) in L:
        res.append(date+' '+imat+' '+src+' '+dest)
    indice = s.menu(res)
    L.pop(int(indice))
    
def charger(chemin):
    vols=[]
    file=open(chemin,'r') 
    for l in file:
        date, imat,src,dest=l.split(' ')
        vols.append((date,imat,src,dest.strip()))
    file.close() 
    return vols

def sauver(chemin,vols):
    file=open(chemin,'w')
    for (date,imat,src,dest) in vols:
        file.write(date+' '+imat+' '+src+' '+dest+'\r')
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
    if a in dico.keys() and b in dico.keys():
        return distance(dico[a],dico[b])
    else:
        return 'Impossible de calculer la distance (ICAO inconnu)'
        
def temps_de_vol(v,distance):
    '''
    temps de vol en minute
    '''
    return distance/(v/60)

def formate_temps(t):
    '''
    Formate t (en minutes) au format HH:MM
    '''
    h = t//60
    m = t-(h*60)
    if h<10:
        h='0'+str(h)
    else:
        h=str(h)
    if m<10:
        m='0'+str(m)
    else:
        m=str(m)
    return str(h)+':'+str(m)

def avant_date(date1,date2):
    '''
    indique si date1 est avant date2
    '''
    d1,m1,a1=date1.split('/')
    d2,m2,a2=date2.split('/')
    date1=datetime.date(int('20'+a1), int(m1), int(d1))
    date2=datetime.date(int('20'+a2), int(m2), int(d2))
    return date1 < date2

print(avant_date('10/08/22','11/07/22'))
    
    

def total_tps_vol(l,dico):
    somme=0
    for (date,_,src,dest) in l:
        d=distance_terrain(src,dest,dico)
        if type(d)==float:
            somme+=temps_de_vol(V,d)
    print('Temps de vol total : '+formate_temps(int(somme)))
    _=input('Appuyez sur [ENTER] pour continuer')
    
def tps_vol_av_date(l,dico):
    date=input('Date (DD/MM/AA) : ')
    somme=0
    for (date_vol,_,src,dest) in l:
        if avant_date(date,date_vol):
            d=distance_terrain(src,dest,dico)
            if type(d)==float:
                somme+=temps_de_vol(V,d)
    print('Temps de vol total : '+formate_temps(int(somme)))
    _=input('Appuyez sur [ENTER] pour continuer')
    
        
