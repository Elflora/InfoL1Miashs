import random

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

def estADN(chaine) :
    '''
    >>> estADN('ATGCGATC')
    True
    >>> estADN('ACKT')
    False
    >>> estADN('ACTK')
    False
    >>> estADN("")
    True
    '''
    save = True
    for i in chaine :
        if i != "A" and i != "T" and i != "C" and i!= "G" :
            save = False
    return save

def genereADN(taille) :
    sequence = ''
    for i in range(taille) :
        sequence += random.choice("ADCT")
    return sequence

def baseComplementaire(lettre) :
    '''
    >>> baseComplementaire('G')
    'C'
    >>> baseComplementaire('T')
    'A'
    '''
    complement = "A"
    if lettre == "G" :
        complement = "C"
    elif lettre == "C" :
        complement = "G"
    elif lettre == "A" :
        complement = "T"
    return complement

def sequenceComplementaireInverse(chaine) :
    '''
    >>> sequenceComplementaireInverse('ACTG')
    'CAGT'
    '''
    complement=""
    for i in chaine :
        complement += baseComplementaire(i)
    save = miroir(complement)
    return save

def motifOccurrences(motif, sequence) :
    '''
    >>> motifOccurrences('ACG', 'GCTACGGAGCTTCGGAGCACGTAG')
    2
    >>> motifOccurrences('TTC', 'AGTCGACTT')
    0
    '''
    j = 3
    save = 0
    for i in range(len(sequence)-2) :
        if sequence[i:j] == motif :
            save += 1
        j+=1
    return save

def ajoutTirets(mot) :
    '''
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

def chiffre(chiffre) :
    '''
    >>> chiffre('0')
    0
    >>> chiffre('4')
    4
    '''
    return int(chiffre)

def entier(entier) :
    '''
    >>> entier('3142')
    3142
    >>> entier('-3142')
    -3142
    >>> entier('+3142')
    3142
    '''
    return int(entier)

def estMajuscule(lettre) :
    '''
    >>> estMajuscule("M")
    True
    >>> estMajuscule("m")
    False
    '''
    maj = False
    if 64<ord(lettre)<91 :
        maj = True
    return maj

def estMinuscule(lettre) :
    '''
    >>> estMinuscule("e")
    True
    >>> estMinuscule("E")
    False
    '''
    min = False
    if 97<ord(lettre)<122 :
        min = True
    return min

def lettreMajuscule(lettre) :
    '''
    >>> lettreMajuscule("e") == "E"
    True
    >>> lettreMajuscule("E") == "E"
    True
    >>> lettreMajuscule("!") == "!"
    True
    >>> lettreMajuscule('vive Python !')
    'VIVE PYTHON !'
    '''
    return lettre.upper()


if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)