from random import choice

def rouleau() :
    '''
    Permet de connaitre la valeur aléatoire d'un rouleau entre les valeur suivante :$, %, #, ~ et &
    
    Retour -> un str ($, %, #, ~ ou &)
    
    Contrainte -> Aucune
    
    tests :
    >>> rouleau()=="$" or rouleau()=="%" or rouleau()=="#" or rouleau()=="~" or rouleau()=="&" 
    True
    >>> rouleau() == ""
    False
    >>> rouleau() == "%$"
    False
    '''
    return choice("$%#~&")

def calculeGain(mise, symbole1,symbole2, symbole3) :
    '''
    Permet de connaitre le gain de la personne grace a la combinaison des trois rouleau et a sa mise
    
    Parametres :
        - mise(int ou float) -> la somme que le joueur met en jeux
        - symbole1(str) -> premier symbole du rouleau (l'un d'eux :$%#~&)
        - symbole2(str) -> deuxieme symbole du rouleau (l'un d'eux :$%#~&)
        - symbole3(str) -> troisieme symbole du rouleau (l'un d'eux :$%#~&)
        
    Retour -> int ou float, le gain de la personne
    
    Contrainte -> Que les valeurs entree soient bonnes
    
    Tests :
    >>> calculeGain(100, "$", "$", "%")
    500
    >>> calculeGain(27.45, "%", "%", "%")
    4117.5
    >>> calculeGain(500, "%", "~", "&")
    0
    '''
    gain = 0
    if symbole1 == "$" and symbole2 == "$" and symbole3 == "$" :
        gain = mise * 250
    elif symbole1 == "%" and symbole2 == "%" and symbole3 == "%" :
        gain = mise * 150
    elif (symbole1 == "$" and symbole2 == "$") or (symbole1 == "$" and symbole3 == "$") or (symbole2 == "$" and symbole3 == "$") :
        gain = mise * 5
    elif (symbole1 == "$") or (symbole2 == "$") or (symbole3 == "$") :
        gain = mise * 2
    return gain

def chaineDifferentiel(mise, gain) :
    '''
    Permet de savoir combien une personne a gagne ou perdue apres avoir joue
    
    Parametres :
     - mise(int ou float) ->la somme de depart que la personne à joue
     - gain(int ou flaot) -> le gain final
     
    Retour -> str, la somme reelle gagner, avec un + ou - devant selon si c'est positif ou negatif
    
    Contraintes ->mise et gain doivent etre des int ou float
    
    Tests :
    >>> chaineDifferentiel(100, 500)
    '+400'
    >>> chaineDifferentiel(25.34, 50.68)
    '+25.34'
    >>> chaineDifferentiel(123, 0)
    '-123'
    '''
    difference = ""
    if gain - mise > 0 :
        difference = "+" + str(gain - mise)
    else :
        difference = gain - mise
    return str(difference)

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
     - le pseudo(str) -> le nom donner par la personne
    
    Contrainte -> Aucune
    '''
    print("Bonjour ", pseudo, ", le but de ce jeux est de mise une somme pour qu'elle soit potentiellement multiplier par 2 au minimum et 250 au maximum")
    
def afficheRouleau(sy1=rouleau(), sy2=rouleau(), sy3=rouleau()) :
    '''
    Permet d'afficher le resultat du tirage
    
    Parametres :
     - sy1(str) -> le premier symbole tiré
     - sy2(str) -> le second symbole tiré
     - sy3(str) -> le troisieme symbole tiré
    
    Contrainte -> Aucune
    '''
    print("Les symboles tirés au sort sont :")
    print(" ----- ----- ----- ")
    print("|  " + sy1 + "  |  " + sy2 + "  |  " + sy3 + "  |")
    print(" ----- ----- ----- ")

def afficheGain(gain) :
    '''
    Permet de dire au joueur combien il a gagner
    
    Parametre :
     - gain(int, float) -> permet de savoir qu'elle est le gain du joueur
     
    Contrainte :gain qui fonctionne
    '''
    if gain > 0 :
        print("Bravo vous avez gagné " + str(gain) + "€  :)")
    else :
        print("Aucun gain, pas de chance :(")
        
def afficheBilan(mise, gain) :
    '''
    Permet de connaitre le differentiel
    
    Parametres :
     - mise(int, float) ->la somme que la personne a mise
     - gain(int, float) ->le gain final
     
    Contraintes -> Que les parametres soient valides
    '''
    print("Par rapport à votre mise initiale, le différentiel est de : " + chaineDifferentiel(mise, gain) + " €")

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)
    
def mainBanditMachot() :
    presentation()
    mise = float(input("Combien souhaitez-vous misez ?"))
    sy1 = rouleau()
    sy2 = rouleau()
    sy3 = rouleau()
    
    gain = calculeGain(mise, sy1, sy2, sy3)
    afficheRouleau(sy1, sy2, sy3)
    afficheGain(float(gain))
    afficheBilan(mise, float(gain))    

mainBanditMachot()