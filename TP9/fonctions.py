from regex import F


def convert_int(m):
    res=''
    for lettre in m:
        try:
            int(lettre)
            res+=lettre
        except:
            ()
    return int(res)

def liste_aeroport():
    res=[]
    f=open('data/airports.txt')
    for ligne in f:
        t = ligne.split()
        print(t)
        temp=t[0]+'-'
        for i in range(3,len(t)):
            temp+=t[i]+' '
        res.append([t[0],temp[0:len(temp)-1]])

    return res
                
        
print(liste_aeroport())