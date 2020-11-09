def affBoucle10() :
    i = 10
    for i in range(10, 21) :
        print(i)
        
def affBoucle0() :
    for i in range(21) :
        print(i)

#range(début du compte inclus, fin du compte exclus, pas)
#range(0, fin du compte OBLIGATOIRE, 1)
        
def sontMinuscule(mot) :
    '''
    Tests :
    >>> sontMinuscule("k")
    True
    >>> sontMinuscule("K")
    False
    >>> sontMinuscule(' ')
    False
    >>> sontMinuscule('des kakis et des kiwis')
    True
    >>> sontMinuscule("des kakis et des kiwis !")
    True
    >>> sontMinuscule("des Kakis et des Kiwi")
    False
    '''
    return mot.islower()

def sommeEntier(n) :
    '''
    >>> sommeEntier(3)
    6
    >>> sommeEntier(10)
    55
    '''
    somme = 0
    for i in range(n+1) :
        somme += i
    return somme

def sommeCarre(n) :
    '''
    >>> sommeCarre(3)
    14
    >>> sommeCarre(10)
    385
    '''
    somme = 0
    for i in range(n+1) :
        somme += i*i
    return somme
        
if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)
