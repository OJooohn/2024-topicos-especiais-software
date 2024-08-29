import turtle

t = turtle.Pen()
t.speed("fastest")

def circulo(nVezes, g):
    for i in range (nVezes):
        t.circle(100)
        t.left(g)

circulo(500, 35)
