import turtle as t

def spirale(size):
    if size < 1: return 1
    
    t.fd(size)
    t.right(90)
    size-=2
    somme = size + spirale(size)
    return somme

t.setheading(90)
t.speed(0)
t.penup()
t.setposition(-400, -400)
t.pendown()
print(spirale(1000))
t.done()