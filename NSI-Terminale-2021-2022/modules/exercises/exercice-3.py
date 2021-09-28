import sys

def somme(a, b):
    return a + b

def produit(a, b):
    return a * b

def puissance(x, n):
    assert type(n) == int
    return x ** n

if __name__ == "__main__":
    a =int(sys.argv[1])
    b = int(sys.argv[2])
    print(somme(a, b))
    print(produit(a, b))
    print(puissance(a, b))