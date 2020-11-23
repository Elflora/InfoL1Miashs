from random import randint
from math import *

def estManque(num) :
    '''
    Permet de savoir si un numeros est manquer
    
    Parametre :
     - num(int) -> le numeros de la roulette
     
    Retour -> Boolean, true si le numeros est manquer
    
    Contrainte -> num valide
    
    Tests :
    >>> estManque(2)
    True
    >>> estManque(35)
    False
    >>> estManque(18)
    True
    '''
    manque = False
    if (num <= 18 ) :
        manque = True
    return manque

def estImpair(num) :
    '''
    Permet de savoir si le nombre tire est impair
    
    Parametre :
     - num(int) -> le numeros aléatoire de la roulette
    
    Retour -> boolean, true si le nombre est impaire
    
    Contrainte -> un num valide
    
    Tests :
    >>> estImpair(2)
    False
    >>> estImpair(35)
    True
    >>> estImpair(3)
    True
    '''
    impaire = True
    if (num % 2 == 0) :
        impaire = False
    return impaire

def lancer() :
    '''
    Simule un lancer aleatoire de la roue et retourne un nombre compris entre 1 et 36
    
    Retour -> un int entre 1 et 36
    
    Contrainte -> Aucune
    
    Tests :
    >>> lancer() >= 1 and lancer() <= 36
    True
    >>> lancer() == 0
    False
    >>> lancer() == -4
    False
    '''
    return randint(1, 36)

def demandeMontant() :
    '''
    Permet de connaitre le montant parier par l'utilisateur
    
    Retour -> un int le montant
    
    Contrainte -> Que la valeur du int soit bonne
    '''
    montant = int(input("Quel est le montant de votre mise ?"))
    return montant

#On espere que l'utilisateur n'essayera pas de faire planter les programmes
def demandeMise() :
    mise = input("Quelle mise voulez-vous faire ?")
    return mise
def calculeGainPari(numRoulette, pari, montant) :
    '''
    Permet de calculer le gain d'un pari
    
    Parametres :
     - numRoulette(int) -> numeros donner par la roulette
     - pari(str) -> pari fais par l'utilisateur
     - montant(int, float) -> montant parier par l'utilisateur
     
    Retour ->le gain fais par la personne
    
    Contraintes -> Que les parametres soient valide
    
    Tests :
    >>> calculeGainPari(6, "Pair", 21)
    42
    >>> calculeGainPari(36, "Passe", 21)
    42
    >>> calculeGainPari(6, "Impair", 21)
    0
    '''
    gain = 0
    if ((pari == "Pair") and not(estImpair(numRoulette))) or ((pari == "Impair") and estImpair(numRoulette)) or ((pari == "Passe") and not(estManque(numRoulette))) or ((pari == "Manque") and estManque(numRoulette)) :
        gain = montant * 2
    return gain
    
def calculeGainNumeros(numRoulette, numeros, montant) :
    '''
    Permet de calculer le gain d'un pari de numeros
    
    Parametres :
     - numRoulette(int) -> numeros donner par la roulette
     - numeros(str) -> pari fais par l'utilisateur
     - montant(int, float) -> montant parier par l'utilisateur
     
    Retour ->le gain fais par la personne
    
    Contraintes -> Que les parametres soient valide
    
    Tests :
    >>> calculeGainNumeros(5, "5", 20)
    720
    >>> calculeGainNumeros(5, "6", 21)
    31
    >>> calculeGainNumeros(5, "31", 21)
    32
    '''
    gain = 0
    numeros = int(numeros)
    if (numeros == numRoulette) :
        gain = montant * 36
    elif (estImpair(numRoulette) and estImpair(numeros)) or (not(estImpair(numRoulette) and (not(estImpair(numeros))))) :
        gain = ceil(montant * 1.5)
    elif (estManque(numRoulette) and estManque(numeros)) or (not(estManque(numRoulette) and (not(estManque(numeros))))) :
        gain = floor(montant * 1.5)
    return gain

def calculeGain(numRoulette, mise, montant) :
    '''
    Permet de calculer le gain d'un pari
    
    Parametres :
     - numRoulette(int) -> numeros donner par la roulette
     - mise(str) -> pari fais par l'utilisateur
     - montant(int, float) -> montant parier par l'utilisateur
     
    Retour ->le gain fais par la personne
    
    Contraintes -> Que les parametres soient valide
    
    Tests :
    >>> calculeGain(6, "Pair", 21)
    42
    >>> calculeGain(36, "Passe", 21)
    42
    >>> calculeGain(6, "Impair", 21)
    0
    >>> calculeGain(5, "5", 20)
    720
    >>> calculeGain(5, "6", 21)
    31
    >>> calculeGain(5, "31", 21)
    32
    '''
    if (int(mise) is None) :
        gain = calculeGainPari(numRoulette, mise, montant)
    else :
        gain = calculeGainNumeros(numRoulette, mise, montant)
    return gain

if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)