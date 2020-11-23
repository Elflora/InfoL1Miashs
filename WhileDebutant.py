import math

def divmod_verbeux(a, b):
    """Affiche les calculs qu'un élève de CE1 ferait pour
    obtenir le quotient et le reste de la division euclidienne
    de a par b.
    Contraintes : a >= 0 et b > 0
    """
    reste = a
    nb_soustractions = 0
    print("Au début, on a fait", nb_soustractions, "soustractions,",
          "et le reste est", reste)
    # début de la boucle
    while reste >= b:
        nb_soustractions = nb_soustractions + 1
        reste = reste - b
        print("Après", nb_soustractions, "soustractions, le reste vaut", reste)
    # fin de la boucle    
    print("Au final, on a fait", nb_soustractions, "soustractions,",
          "et le reste est", reste)
    
def reste(a, b) :
    '''
    >>> reste(5, 5)
    0
    >>> reste(42, 5)
    2
    >>> reste(3, 4)
    3
    '''
    reste = a
    while reste >= b :
        reste -= b
    return reste

def quotient(a, b) :
    '''
    >>> quotient(5, 5)
    1
    >>> quotient(42, 5)
    8
    >>> quotient(3, 4)
    0
    '''
    reste = a
    quotient = 0
    while reste >= b :
        reste -= b
        quotient += 1
    return quotient

def est_ADN(chaine):
    '''
    >>> est_ADN('ATGCGATC')
    True
    >>> est_ADN('ACKT')
    False
    >>> est_ADN('ACTK')
    False
    >>> est_ADN("")
    True
    '''
    adn=True
    i = 0
    while i != len(chaine) and adn:
        if not( chaine[i] in 'ATCG') :
            adn = False
        i+=1
    return adn

def croissanceBlob(tailleInit) :
    jour = 0
    while tailleInit < 1 :
        tailleInit *= 2
        jour += 1
    return jour

def nbPeriodRadioactive(partDisparue) :
    '''
    >>> nbPeriodRadioactive(0.75)
    2
    '''
    part = math.ceil(partDisparue)
    reste = part - partDisparue
    nbPeriodeRadio = 0
    
    while part > reste :
        part = part / 2
        nbPeriodeRadio += 1
    return nbPeriodeRadio

def racineCarreEntier(entier) :
    i = 0
    while i <= entier**2 :
        i+=1
    return i

def racineHeron(x, epsilon) :
    un = (epsilon + (x / epsilon))/2
    return (un - (x/un)) < epsilon
    
    
#Essayer séparé fonction
def volSyracuse(n) :
    '''
    >>> volSyracuse(14)
    52
    >>> volSyracuse(1024)
    1024
    >>> volSyracuse(871)
    190996
    '''
    terme = n
    max = terme
    while terme > 1 :
        if terme % 2 == 0:
            terme = terme // 2
        else:
            terme = terme * 3 + 1
        if max < terme :
            max = terme
    return max



if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)