import turtle as t

def koch(n, l=400):
    """
    Dessine la fractale du flocon de Von Koch
    n : Nombre d'itérations
    l : longueur d'un segment (default=400)
    """
    t.speed(0)
    if n == 0:
        t.fd(l) 
        return
    koch(n-1, l/3)
    t.left(60)
    koch(n-1, l/3)
    t.right(120)
    koch(n-1, l/3)
    t.left(60)
    koch(n-1, l/3)

def flocon(n, l=400):
    for _ in range(3):
        koch(n, l)
        t.right(120)
    t.done()

def tree(longueur=100):
    if longueur < 10: return

    t.fd(longueur)
    t.left(45)
    tree(longueur * 0.6)
    t.right(90)
    tree(longueur * 0.6)
    t.left(45)
    t.fd(-longueur)
    return

if __name__ == "__main__":
    koch(3)
    flocon(3)
    tree()
    t.done()