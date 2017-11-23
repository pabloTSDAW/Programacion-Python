import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('normal')
t.pen(pencolor='blue', fillcolor='green')

#Apartado a

def poligono(lado, vertices):
    """Crea un polígono de lado=lado"""
    for i in range(vertices):
        t.fd(lado)
        t.left(360/vertices)
        

#Apartado b
        
def circulo_poligono(lado, vertices):
    """Crea un círculo de poligonos"""
    for i in range(vertices):
        poligono(lado, vertices)
        t.up()
        t.rt(360/vertices)
        t.fd(50)
        t.down()

#Apartado c
        
def circulo_creciente(lado, vertices, circulos):
    """Crea un círculo de poligonos crecientes"""
    for j in range(1, circulos+1):
        for i in range(vertices):
            poligono(lado*j, vertices)
            t.up()
            t.rt(360/vertices)
            t.fd(50)
            t.down()
    
