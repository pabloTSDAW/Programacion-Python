import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed(1)
t.pen(pencolor='blue', fillcolor='green')
t.speed(5)
t.up()
t.setpos(-200,0)
t.down()

puntos = []

def monte(x, y):
    t.up()
    t.setpos(x)
    t.down()
    puntos.append(t.position())
    dis = t.distance(y)/3
    t.fd(dis)
    puntos.append(t.position())
    t.lt(60)
    t.fd(dis)
    puntos.append(t.position())
    t.rt(120)
    t.fd(dis)
    puntos.append(t.position())
    t.lt(60)
    t.fd(dis)
    puntos.append(t.position())

    
monte((-100,0), (100,0))
t.clear()
puntos.sort()


def generacion(n):
    for i in range(0, len(puntos)-1):
        print(t.heading())
        if t.heading() == 0:
            monte(puntos[i], puntos[i+1])
            t.lt(60)
        elif t.heading() == 60:
            monte(puntos[i], puntos[i+1])
            t.lt(-120)
        elif t.heading() == 300:
            monte(puntos[i], puntos[i+1])
            t.lt(60)
        elif t.heading() == 120:
            monte(puntos[i], puntos[i+1])
            t.lt(120)
    t.rt(60)
    set(puntos)
    puntos.sort()
    puntos.pop()
    puntos.remove((-100.00,0.00))
    t.clear()

generacion(2)




