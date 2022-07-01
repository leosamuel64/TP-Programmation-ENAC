from random import *

nb_tour=int(input('Nombre de tour : '))
j1 = input("Nom du joueur 1 : ")
j2 = input("Nom du joueur 2 : ")

score_j1=0
score_j2=0

numtour=0
     

while numtour<nb_tour:
    print('Tour ',numtour)
    # Tour de j1
    t1,t2=randint(1,6), randint(1,6)
    if t1==t2:
        score_j1+=1
    print(j1,' ',t1,',',t2,'score = ',score_j1)

    # Tour de j2
    t1,t2=randint(1,6), randint(1,6)
    if t1==t2:
        score_j2+=1
    print(j2,' ',t1,',',t2,'score = ',score_j2)

    numtour+=1

if score_j1>score_j2:
    print('Le gagnant est ', j1)
elif score_j2>score_j1:
    print('Le gagnant est ', j2)
else:
    print("Match nul")
