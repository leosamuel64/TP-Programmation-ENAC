from asyncore import read
import fonctionsVols as v
import simui as s



def main(chemin):
    continuer = True
    vols = v.charger(chemin)

    while continuer:
        print("\t\t\t ------- MENU -------")
        print("\t\t\t Quit               Q")
        print("\t\t\t Afficher Vols      P")
        print("\t\t\t Ajouter Vol        A")
        print("\t\t\t Supprimer Vol      S")
        print("\t\t\t --------------------");

        choice = input("\t\t\t Your choice? ").upper()

        match choice:
            case 'Q':
                continuer=False    
            case 'P':
                v.afficherVol(vols)
            case 'A':
                v.ajoutVol(vols)
            case 'S':
                v.supprimeVol(vols)

# main()


def main_Menu(chemin,chdico):
    continuer = True
    vols = v.charger(chemin)
    dico=v.charge_terrain(chdico)

    while continuer:
        choice = s.menu(['Quit','Afficher Vols', 'Ajouter Vol', 'Supprimer Vol','Total temps de vol','Temps de vol après une date'])

        match choice:
            case 0:
                continuer=False
            case 1:
                v.afficherVol(vols,dico)
            case 2:
                v.ajoutVol(vols)
                v.sauver(chemin, vols)
            case 3:
                v.supprimeVol2(vols)
                v.sauver(chemin, vols)
            case 4:
                v.total_tps_vol(vols,dico)
            case 5:
                v.tps_vol_av_date(vols,dico)
                
main_Menu('Python/TP6/flights.txt','Python/TP6/airports.txt')
