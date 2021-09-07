import turtle as t

def Arbre(longueur=100):
    if longueur < 10: return

    t.fd(longueur)
    t.left(30)
    Arbre(longueur * 0.6)
    t.right(60)
    Arbre(longueur * 0.6)
    t.left(30)
    t.fd(-longueur)
    return

Arbre(200)
t.done()