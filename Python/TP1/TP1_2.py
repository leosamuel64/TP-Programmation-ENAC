def est_bissextile(a):
    div4=False
    div100=False
    div400=False
    if a%4==0:
        div4=True
    if a%100==0:
        div100=True
    if a%400==0:
        div400=True
    if div4 and not div100:
        res=True
    elif div400:
        res=True
    else:
        res=False
    return res

def numero_jour(jour,mois,année):
    if est_bissextile(année):
        feb=29
    else:
        feb=28
    nb=[31,feb,31,30,31,30,31,31,30,31,30,31]

    res=0

    for i in range(0,mois):
        res+=nb[i]

        return res+jour





jour = int(input("Jour : "))
mois = int(input("Mois : "))
année = int(input("Année : "))

res=True

if jour not in range(1,32):
    res= False
if mois not in range(1,13):
    res=False
if jour==31 and (mois not in [1,3,5,7,8,10,12]):
    res=False
if mois==2 and not est_bissextile(année) and jour>28:
    res=False

jours=["samedi","dimanche","lundi","mardi","mercredi","jeudi","vendredi"]




if res:
    num=numero_jour(jour,mois,année)
    semaine=jours[num%7]
    print(res,semaine)
else:
    print(res)

