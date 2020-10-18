from random import randint

def de() :
    '''
    Permet de lancer un de allant de 1 à 6
    
    Retour -> un int entre 1 et 6
    
    Contrainte -> Aucune
    
    tests :
    >>> de()==1 or de()==2 or de()==3 or de()==4 or de()==5 or de()==6
    True
    >>> de() == 0
    False
    >>> de() == ""
    False
    '''
    return randint(1, 6)

def est_un_421(a, b, c) :
    '''
    Permet de savoir si les trois chiffres tires donne un 4 2 1(qu'importe l'ordre)
    
    Parametres :
     - a(int) -> premier dè tire (1d6)
     - b(int) -> second dè tire (1d6)
     - c(int) -> troisieme dè tire (1d6)
     
    Retour -> un boolean, donnant vrai si a, b, c forment un 421
    
    Contraintes : -> que a, b, c soient valident
    
    Tests :
    >>> est_un_421(2, 1, 4)
    True
    >>> est_un_421(4, 2, 3)
    False
    >>> est_un_421(3, 5, 6)
    False
    '''
    save = False
    if a==4 and ((b==2 and c==1) or (b==1 and c==2)) :
        save = True
    elif a==2 and ((b==4 and c==1) or (b==1 and c==4)) :
        save = True
    elif a==1 and ((b==4 and c==2) or (b==2 and c==4)) :
        save = True
    return save    

def identification() :
    '''
    Permet de connaitre le nom de la personne
    
    Retour -> un str, le pseudo
    
    Contrainte -> Aucune
    '''
    pseudo = input("Qu'elle est ton nom ?")
    return pseudo

def presentation(pseudo=identification()) :
    '''
    Permet de saluer le joueur et lui expliquer les regles
    
    Parametre :
     - le pseudo, str, le nom donner par la personne
     
    Retour ->str, qui presente le jeux
    
    Contrainte -> Aucune
    '''
    print("Bonjour ", pseudo, " Le but de ce jeux est de lancer 3d6 qui forme un 421")

def poursuivreLeJeux() :
    '''
    Permet de savoir si le joueur souhaite jouer
    
    Retour ->un booleen, True si la personne souhaite jouer
    
    Contrainte -> répondre "oui" pour jouer
    
    Tests :
    Comment faire pour tester l'input ?
    '''
    poursuivre = input("Voulez-vous jouer ? (oui_non)")
    if (poursuivre=="oui") :
        return True
    return False

def afficheLancer(a, b, c) :
    '''
    Permet d'afficher les lancer des 3d6
    
    Parametres :
     - a(int) -> premier dè tire (1d6)
     - b(int) -> second dè tire (1d6)
     - c(int) -> troisieme dè tire (1d6)
     
    Contraintes -> que les parametres soient valides
    '''
    print("+---+   +---+   +---+")
    print("|", a, "|   |", b, "|   |", c, "|")
    print("+---+   +---+   +---+")
    
def afficheResultat(a, b, c) :
    '''
    Permet d'afficher si la personne a gagne ou perdue
    
    Paramtres :
     - a(int) -> premier dè tire (1d6)
     - b(int) -> second dè tire (1d6)
     - c(int) -> troisieme dè tire (1d6)
     
     Contrainte -> que les parametres soient valides
    '''
    if est_un_421(a, b, c) :
        print("~~VICTOIRE~~")
    else :
        print("DEFAITE...")

def main_421() :
    presentation()
    if (poursuivreLeJeux()) :
        a, b, c = de(), de(), de()
        afficheLancer(a, b, c)
        afficheResultat(a, b, c)
    else :
        print("Au revoir")

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)

main_421()




