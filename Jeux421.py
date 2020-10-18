from random import randint

def de() :
    return randint(1, 6)

def est_un_421(a, b, c) :
    save = False
    if a==4 and ((b==2 and c==1) or (b==1 and c==2)) :
        save = True
    elif a==2 and ((b==4 and c==1) or (b==1 and c==4)) :
        save = True
    elif a==1 and ((b==4 and c==2) or (b==2 and c==4)) :
        save = True
    return save    

def identification() :
    pseudo = input("Qu'elle est ton nom ?")
    return pseudo

def presentation(pseudo=identification()) :
    print("Bonjour ", pseudo, " Le but de ce jeux est de lancer 3d6 qui forme un 421")

def poursuivreLeJeux() :
    poursuivre = input("Voulez-vous jouer ? (oui_non)")
    if (poursuivre=="oui") :
        return True
    return False

def afficheLancer(a, b, c) :
    print("+---+   +---+   +---+")
    print("|", a, "|   |", b, "|   |", c, "|")
    print("+---+   +---+   +---+")
    
def afficheResultat(a, b, c) :
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
        
main_421()

#if __name__ == '__main__' :
#    import doctest
#    doctest.testmod(verbose = True)






