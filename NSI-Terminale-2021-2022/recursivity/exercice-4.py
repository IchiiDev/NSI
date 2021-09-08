import turtle as t
from random import randint as rn

colors = ("blue", "red", "green", "yellow", "brown", "pink", "orange", "purple") 

def Arbre(longueur=100, steps=1):
    if longueur < 10: return

    t.color(colors[rn(0, len(colors) - 1)])
    t.width(5/steps)
    t.fd(longueur)
    t.left(45)
    Arbre(longueur * 0.6)
    t.right(90)
    steps+=1
    Arbre(longueur * 0.6, steps)
    t.left(45)
    t.fd(-longueur)
    return

t.setheading(90)
t.speed(0)
t.setposition(0, -300)
Arbre(300)
t.done()