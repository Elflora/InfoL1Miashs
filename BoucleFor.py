from math import sqrt
from math import factorial

def carreParfait1(n) :
    '''
    Permet de savoir si un carre est parfait en fonction de n son aire
    
    Parametre : n un int, est l'air du carré
    
    Retour -> True si c'est un carre parfait
    
    Contrainte -> Que n soit un int
    
    Exemples :
    >>> carreParfait1(9)
    True
    >>> carreParfait1(6)
    False
    >>> carreParfait1(49)
    True
    '''
    save = False
    for i in range(n) :
        if i*i == n :
            save = True
    return save

def carreParfait2(n) :
    '''
    Permet de savoir si un carre est parfait en fonction de n son aire
    
    Parametre : n un int, est l'air du carré
    
    Retour -> True si c'est un carre parfait
    
    Contrainte -> Que n soit un int
    
    Exemples :
    >>> carreParfait2(9)
    True
    >>> carreParfait2(6)
    False
    >>> carreParfait2(49)
    True
    '''
    racine = sqrt(n)
    if racine.is_integer() :
        return True
    return False

def racineEntiere(n) :
    '''
    Permet de connaitre l'entier supérieur ou égal a la racine
    
    Parametre : n un int, est l'air du carré
    
    Retour -> int
    
    Contrainte -> Que n soit un int
    
    Exemples :
    >>> racineEntiere(15)
    4
    >>> racineEntiere(14)
    4
    >>> racineEntiere(17)
    4
    '''
    return round(sqrt(n))
    
def estPremier(n) :
    '''
    >>> estPremier(2)
    True
    >>> estPremier(6)
    False
    >>> estPremier(13)
    True
    >>> estPremier(79)
    True
    '''
    save = True
    for i in range(2, n-1) :
        if n%i == 0 :
            save = False
    return save

def listeDesPremiers(a,b) :
    for a in range(a, b) :
        if estPremier(a) :
            print(a)

def combienPremier(a, b) :
    save = 0
    for i in range(a+1, b) :
        if estPremier(i) :
            save += 1
    return save

#str()

def sommeNombre1(n) :
    nombre = str(n)
    save = 0
    for i in nombre :
        save += int(i)
    return save

def sommeNombre2(n) :
    s = 0
    copyn = n
    k = len(str(n))
    for i in range(k) :
        s+=copyn%10
        copyn = copyn//10
    return s

def sommeFactorielle(n) :
    save = 0
    for i in str(n) :
        save += factorial(int(i))
    return save

def egaux(n) :
    return sommeFactorielle(n) == n

def toutEgaux(n) :
    for i in range(n) :
        if egaux(i) :
            print(i)

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)
