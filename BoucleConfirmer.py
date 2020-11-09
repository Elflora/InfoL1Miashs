#PAS FINI

def enMajuscules(phrase) :
    '''
    >>> enMajuscules('des kakis et des kiwis')
    'DES KAKIS ET DES KIWIS'
    >>> enMajuscules('des kakis et des kiwis !')
    'DES KAKIS ET DES KIWIS !'
    >>> enMajuscules('des Kakis et des Kiwis')
    'DES KAKIS ET DES KIWIS'
    >>> enMajuscules('')
    ''
    '''
    save = ""
    for i in phrase :
        save+= i.upper()
    return save

def enCapitale(phrase) :
    '''
    >>> enCapitale('des kakis et des kiwis')
    'Des Kakis Et Des Kiwis'
    >>> enCapitale('Des Kakis Et Des Kiwis')
    'Des Kakis Et Des Kiwis'
    >>> enCapitale('DES KAKIS ET DES KIWIS')
    'DES KAKIS ET DES KIWIS'
    >>> enCapitale('')
    ''
    '''
    if len(phrase) > 0 :
        save = phrase[0].upper()
        for i in range(1, len(phrase)) :
            if phrase[i-1] == " " :
                save+=phrase[i].upper()
            else :
                save += phrase[i]
    else : save = ''
    return save

def miroir(phrase) :
    '''
    >>> miroir('Python')
    'nohtyP'
    >>> miroir('super')
    'repus'
    >>> miroir('')
    ''
    '''
    save = ''
    for i in range(len(phrase)-1, -1, -1) :
        save += phrase[i]
    return save

def plusLong(mot1, mot2) :
    if len(mot1) - len(mot2) == 0 :
        save = mot1
    elif len(mot1) - len(mot2) > 0 :
        save = mot1
    else :
        save = mot2
    return save

def anacycliques(mot1, mot2) :
    '''
    >>> anacycliques('zen', 'nez')
    True
    >>> anacycliques("l'ami naturel", 'le rut animal')
    True
    '''
    mot1 = miroir(mot1)
    longueur = plusLong(mot1, mot2)
    save = True
    
    for i in range(len(longueur)) :
        if mot1[i] != mot2[i] :
            save = False
    return save

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)