#Capentier Madeline

def ajoutTirets(mot) :
    '''
    Permet d'ajouter des tirer entre chaque lettre d'un mot
    
    Parammetre :
     - mot, str, mot ou phrase passer en parametre
     
     Contraintes : Aucune
     
     Retour : un str
     
    Tests :
    >>> ajoutTirets("Bonjour") == "B-o-n-j-o-u-r-"
    True
    >>> ajoutTirets("a") == "a-"
    True
    >>> ajoutTirets("") == ""
    True
    '''
    save = ""
    for i in mot :
        save += i + "-"
    return save

def supprimeCara(mot, lettre) :
    '''
    Permet de supprimer une lettre d'un mot/phrase
    
    Parametre :
     - mot, un str
     - lettre, char, la lettre a spprimer
     
    Contrainte : Pas de chiffre
    
    Retour : un str
    
    Tests :
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
    Permet de savoir si une phrase est un palindrome
    
    Parametre : phrase, str, une phrase qui pourrait etre un palindrome
    
    Contraintes : donner un str
    
    Retour : booleen vrai si une phrase est un palindrome
    
    Tests :
    >>> estPhrasePalindrome("eh ca va la vache")
    True
    >>> estPhrasePalindrome("engage le jeu que je le gagne")
    True
    >>> estPhrasePalindrome("Engage le jeu que je le gagne.")
    False
    '''
    phrase = supprimeCara(phrase, " ")
    return estPalindrome1(phrase)

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)