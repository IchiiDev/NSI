import turtle as t

def spirale(size):
    if size < 1: return
    
    t.fd(size)
    t.right(90)
    size-=1
    spirale(size)
    return

t.setheading(90)
t.speed(0)
t.penup()
t.setposition(-300, -200)
t.pendown()
spirale(500)
t.done()