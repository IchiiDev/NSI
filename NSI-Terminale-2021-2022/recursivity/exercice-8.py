import turtle as t

def fractale(n, l=400):
    if n == 0:
        t.fd(l) 
        return
    fractale(n-1, l/3)
    t.left(60)
    fractale(n-1, l/3)
    t.right(120)
    fractale(n-1, l/3)
    t.left(60)
    fractale(n-1, l/3)

t.speed(0)
fractale(3)
t.done()