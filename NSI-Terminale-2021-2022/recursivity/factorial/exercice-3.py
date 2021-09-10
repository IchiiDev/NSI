def somme(liste):
    if len(liste) == 0: return 0
    print(liste[1:])
    return liste[0] + somme(liste[1:])

liste = [3, 7, 5, 10, 8, 7]
print(somme(liste))