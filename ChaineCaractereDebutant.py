# ord(lettre) -> numeros ascii
# chr(nombre) -> lettre ascii qui correspond
# mot1 > mot2 -> comparaison mot dico

def maximum(m1, m2) :
    save = m2
    if len(m1) > len(m2) :
        save = m1
    return save

def minimum(m1, m2) :
    save = m2
    if len(m1) < len(m2) :
        save = m1
    return save

#Travailler avec des tableau beaucoup plus pratique

def miroir(chaine) :
    '''
    >>> miroir("abc") == "cba"
    True
    >>> miroir("") == ""
    True
    >>> miroir("a") == "a"
    True
    >>> miroir('bonjour') == 'ruojnob'
    True
    >>> miroir("Vive Zorglub !") == '! bulgroZ eviV'
    True
    '''
    save = ''
    longueur = len(chaine)
    for i in range(longueur-1, -1, -1) :
        save += chaine[i]
    return save

def miroir2(chaine) :
    '''
    >>> miroir("abc") == "cba"
    True
    >>> miroir("") == ""
    True
    >>> miroir("a") == "a"
    True
    >>> miroir('bonjour') == 'ruojnob'
    True
    >>> miroir("Vive Zorglub !") == '! bulgroZ eviV'
    True
    '''
    resu = ""
    for c in chaine :
        resu = c + resu
    return resu

def unSurDeux(chaine) :
    '''
    >>> unSurDeux("abc") == "ac"
    True
    >>> unSurDeux("") == ""
    True
    >>> unSurDeux("a") == "a"
    True
    >>> unSurDeux('bonjour') == 'bnor'
    True
    >>> unSurDeux("Vive Zorglub !") == 'Vv ogu '
    True
    '''
    save = ""
    for i in range(len(chaine)) :
        if i%2 == 0 :
            save += chaine[i]
    return save

def un_caractere_sur_deux(s):
    '''
    >>> un_caractere_sur_deux("abc") == "ac"
    True
    >>> un_caractere_sur_deux("") == ""
    True
    >>> un_caractere_sur_deux("a") == "a"
    True
    >>> un_caractere_sur_deux('bonjour') == 'bnor'
    True
    >>> un_caractere_sur_deux("Vive Zorglub !") == 'Vv ogu '
    True
    '''
    unsurdeux=''
    for i in range(0,len(s),2):
        unsurdeux+=s[i]
    return unsurdeux

def dernierIndiceCara(chaine, lettre) :
    '''
    >>> dernierIndiceCara("Bonjour", "B") == 0
    True
    >>> dernierIndiceCara("Bonjour", "o") == 4
    True
    >>> dernierIndiceCara("Bonjour", "r") == 6
    True
    '''
    save = "" #peu utile
    for i in range(len(chaine)) :
        if chaine[i] == lettre :
            save = i
    return save

def premierIndiceCara(chaine, lettre) :
    '''
    >>> premierIndiceCara("Bonjour", "B") == 0
    True
    >>> premierIndiceCara("Bonjour", "o") == 1
    True
    >>> premierIndiceCara("Bonjour", "r") == 6
    True
    '''
    trouver = False
    save = 0
    for i in range(len(chaine)) :
        if (chaine[i] == lettre) and (not trouver) :
            save = i
            trouver = True
    return save

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)