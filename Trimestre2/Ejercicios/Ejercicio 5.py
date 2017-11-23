import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.speed('normal')
s.setup(400,300,0,0)
s.screensize(400,300)

#Apartado 0

def medidas(tortuga):
    t.shapesize()

    
#Apartado a

t.shape('square')

def rebote(num):
    """Hace que la tortuga rebote con los límites de la ventana"""
    for i in range(num):
        t.up()
        t.fd(400)
        t.back(800)
        t.goto(0,0)

#Otra forma, más elaborada
        
def rebote2(num):
    """Hace que la tortuga rebote con los límites de la ventana"""
    t.up()
    for i in range(num):
        while t.xcor() != 400:
            t.fd(10)
        while t.xcor() != -400:
            t.back(10)


    


