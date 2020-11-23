#C'est bien parenthésé si le compteur n'est jamais négatif

def nbParenthese(chaine) :
    '''
    >>> nbParenthese("(()())")
    0
    >>> nbParenthese("(()()")
    1
    >>> nbParenthese("(()))(")
    0
    '''
    parenthese = 0
    for i in chaine :
       parenthese += numParenthese(i)
    return parenthese

def numParenthese(une) :
    save = 0
    if une == '(' :
        save += 1
    else :
        save -= 1
    return save

def bienParenthese(chaine) :
    '''
    >>> bienParenthese("(()())")
    True
    >>> bienParenthese("(()()")
    False
    >>> bienParenthese("(()))(")
    False
    '''
    save = False
    if nbParenthese(chaine) == 0 :
        if chaine[-1] == ')' :
            save = True
    return save
    
def nbrFacteur(parenthese) :
    '''
    >>> nbrFacteur("(()())")
    1
    >>> nbrFacteur("()(()())")
    2
    >>> nbrFacteur("(())()(()())")
    3
    '''
    compte = 0
    fact = 0
    for i in parenthese :
        compte += numParenthese(i)
        if compte == 0 :
            fact += 1
    return fact

def decoupeFacteurs(parenthese) :
    '''
    >>> decoupeFacteurs('(()())') == '(()())'
    True
    >>> decoupeFacteurs('(())()(()())') == '(())*()*(()())'
    True
    '''
    compte = 0
    save = ""
    ite = 0
    for i in parenthese :
        compte += numParenthese(i)
        save += i
        ite += 1
        if compte == 0  and ite < len(parenthese):
            save += "*"
    return save
    
if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)