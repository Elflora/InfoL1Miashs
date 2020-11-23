def estPremierNaif(p) :
    '''
    >>> estPremierNaif(1)
    False
    >>> estPremierNaif(13)
    True
    >>> estPremierNaif(2020)
    False
    '''
    premier = True
    i = 2
    if p < 2 :
        premier = False
    while i <= (p-1) and premier :
        if p%i == 0 :
            premier = False
        i+=1
    return premier

def auMoinUnPremier(intervalle) :
    '''
    >>> auMoinUnPremier(range(12))
    True
    >>> auMoinUnPremier(range(8, 11))
    False
    '''
    premier = False
    i = 2
    while i in intervalle and not premier:
        if estPremierNaif(i) :
            premier = True
            break
    return premier


if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)