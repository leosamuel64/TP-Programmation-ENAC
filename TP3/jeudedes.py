from random import *

def identique(t):
    """
    Indique si tout les éléments d'un tableau sont identiques
    """
    i=t[0]
    res=True
    for n in t:
        if i!=n:
            res=False
    return res


def jouer(joueur, nb_de_dés, score):
    """
    Lance les dés pour un joueur, calcul le nouveau score et fair l'affichage pour ce joueur
    """
    lancements=[randint(1,6) for _ in range(nb_de_dés)]
    if identique(lancements):
        score[joueur]+=1

    print(joueur,'-', lancements,'- score = ',score[joueur])


def est_gagnant(score):
    """
    Vérifie si un joueur a gagné et l'indique (sinon -1)
    """
    copy=[i for i in score]
    copy.sort(reverse=True)
    if copy[0]>copy[1]+4:
        res=True
        for i in range(len(score)):
            if score[i]==copy[0]:
                gagnant=i
    else:
        res=False
        gagnant=-1

    return res,gagnant


def jeu(nb_joueur,nb_tour,nb_dés):
    """
    Fonction principale du jeu
    """
    score=[0 for _ in range(nb_joueur)]
    gagnant_present=False
    tour=0

    while tour<=nb_tour and not gagnant_present:
        print("----- Tour : ",tour," -----")
        for joueur in range(nb_joueur):
            jouer(joueur, nb_dés, score)
        
        gagnant_present, gagnant =  est_gagnant(score)
        tour+=1

    if gagnant_present:
        print('Le gagant est : ',gagnant)
    else:
        print('Match nul')





jeu(5,100000,5)
