from JeuxBanditManchot import mainBanditMachot
from Jeux421 import main_421
#Permet d'importer le jeux bandit manchot
#Etrange : il lance par default les deux jeux importer avant de lancer le main
        
def main_games() :
    print('Jouons ensemble\n')
    jeu = input('À quel jeu voulez-vous jouer ? A   B  (A si "Jeux421" B si "bandit manchot"')
    if (jeu == 'A') :
        main_421()
    elif (jeu == 'B') :
        mainBanditMachot()
                    
if __name__ =='__main__':
    main_games()