def invert(chaine):
    if len(chaine) == 1: return chaine[0]
    return invert(chaine[1:]) +  chaine[0]

print(invert("Python, c'est un langage de programmation"))