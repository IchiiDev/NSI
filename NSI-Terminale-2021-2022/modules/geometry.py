from math import pi

"""
Module de calcul des aires
"""

def aireCarre(x):
    """
    Calculer l'aire d'un carré
    n : longueur d'un côté
    retour : aire du carré
    """
    return x * x

def aireTriangle(b, h):
    """
    Calculer l'aire d'un triangle
    b : base du triangle
    h : hauteur du triangle
    retour : aire du triangle
    """
    return (b * h) / 2

def aireTrapese(B, b, h):
    """
    Calculer l'aire d'un trapèse
    B : grande base
    b : petite base
    h : hauteur
    retour : aire du triangle
    """
    return ((B + b) * h) / 2

def aireDisque(r):
    return (r**2) * pi

print("Module de calcul des aires chargé")