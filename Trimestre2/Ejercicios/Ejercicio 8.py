import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('normal')
t.pen(pencolor='blue', fillcolor='green')
t.up()
t.setpos(-200,0)
t.down()

#Apartado a

lista = []

def segmento(lon):
    """Divide el segmento en 3 partes y guarda esos puntos en una lista"""
    for i in range(4):
        t.fd(lon/4)
        lista.append(t.position())

def generacion():
    """Divide el segmento en 3 partes y guarda esos puntos en una lista"""
    for i in range(0,3):
        t.setpos(lista[i])
        segmento(t.distance(lista[i+1]))
    for i in lista:
        t.setpos(lista[1])
        t.lt(60)
        t.fd(t.distance(lista[i+1]))
        t.rt(120)
        t.fd(t.distance(lista[i+1]))
        t.lt(60)

def generacion2():
    for i in range(0, len(lista)):
        t.up()
        t.setpos(lista[i])
        t.down()
        dis = t.distance(lista[1])
        for i in range(1):
            t.fd(dis)
            t.lt(60)
            t.fd(dis)
            lista.append(t.position())
            t.rt(120)
            t.fd(dis)
            lista.append(t.position())
            t.lt(60)
            t.fd(dis)
        

def triangulo():
    for i in range(1):
        t.fd(t.distance(lista[i]))
        t.left(60)
        t.fd(t.distance(lista[i]))
        t.rt(120)
        t.fd(t.distance(lista[i]))
        t.left(60)
        t.fd(t.distance(lista[i]))

def equilateros():
    for i in range(3):
        pass

segmento(400)
t.clear()
generacion2()

