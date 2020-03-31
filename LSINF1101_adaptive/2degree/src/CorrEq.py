def racine_carree(n):
    """
    Calcule une racine carree
    pre: n est un nombre réel
         n >= 0
    post: retourne la racine carrée réelle de n
    """
    import math
    return math.sqrt(n)

def rho(a, b, c):
    return b*b-4*a*c

def n_solutions(a, b, c):
    r = rho(a, b, c)
    if r < 0:
        return 0
    return 1 if r == 0 else 2

def solution(a, b, c):
    """ pre: l'equation definie par a, b, c comporte au moins une solution """
    if n_solutions(a, b, c) == 1:
        return -b/(2*a)
    r = rho(a, b, c)
    return min((-b + racine_carree(r))/(2*a), (-b - racine_carree(r))/(2*a))