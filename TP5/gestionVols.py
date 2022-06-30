from asyncore import read
import fonctionsVols as v
import simui as s



def main(chemin):
    continuer = True
    vols = []
    
   

    while continuer:
        # Print menu
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


def main_Menu(chemin):
    continuer = True
    vols = []

    file=open(chemin,'r') 
    lignes=file.readlines()
    for l in lignes:
        imat,src,dest=l.split(';')
        vols.append((imat,src,dest.strip()))
    file.close() 

    while continuer:
        # Print menu
        choice = s.menu(['Quit','Afficher Vols', 'Ajouter Vol', 'Supprimer Vol'])

        match choice:
            case 0:
                continuer=False
                file=open(chemin,'w')
                for (imat,src,dest) in vols:
                    file.write(imat+';'+src+';'+dest+'\r')
                file.close()
            case 1:
                v.afficherVol(vols)
            case 2:
                v.ajoutVol(vols)
            case 3:
                v.supprimeVol2(vols)
                
main_Menu('TP5/file.csv')
