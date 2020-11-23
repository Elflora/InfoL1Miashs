def sontMinuscules(phrase) :
    '''
    >>> sontMinuscules("Bonjour")
    False
    >>> sontMinuscules("il y a un chat")
    True
    '''
    return phrase.islower()

def supprimeCara(mot, lettre) :
    #Ici un for est plus insterressant car pour être sur de ne pas avoir oublier de caractére il faut parcourir toute la bouble
    '''
    >>> supprimeCara("valeur de la chaine", " ") == 'valeurdelachaine'
    True
    >>> supprimeCara("test", "t") == "es"
    True
    >>> supprimeCara("test", "a") == "test"
    True
    '''
    save = ""
    for i in mot :
        if i != lettre :
            save += i
    return save

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
    #Aucun interet a mettre un while on parcour en entier dans tout les cas
    save = ''
    if len(chaine) > 0 :
        longueur = len(chaine)
        for i in range(longueur-1, -1, -1) :
            save += chaine[i]
    return save

def estPalindrome1(mot) :
    '''
    >>> estPalindrome1("ici")
    True
    >>> estPalindrome1("Bonjour")
    False
    >>> estPalindrome1("radar")
    True
    '''
    return miroir(mot) == mot

def estPhrasePalindrome(phrase) :
    '''
    >>> estPhrasePalindrome("eh ca va la vache")
    True
    >>> estPhrasePalindrome("engage le jeu que je le gagne")
    True
    >>> estPhrasePalindrome("Engage le jeu que je le gagne.")
    False
    '''
    phrase = supprimeCara(phrase, " ")
    return estPalindrome1(phrase)

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


if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)