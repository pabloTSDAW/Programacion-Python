import turtle

pantalla = turtle.Screen()
pantalla.screensize(400, 300)
pantalla.setup(width=1000, height=800, startx=270, starty=0)
pantalla.bgcolor("green")

color = 'orange'
puntos= []
volver = 'Menu/volver.gif'

pantalla.register_shape(volver)


def lista_puntuaciones():
    dic = {}
    f = open('Score.txt', 'r')
    linea = f.readline()
    while linea != '':   #Con bucle while es más eficiente
        linea = linea.strip('\n')
        linea = linea.split()
        puntos.append(linea)
        dic[int(linea[1])] = linea[0]
        linea = f.readline()
    lista = list(dic.keys())
    lista.sort()
    lista.reverse()
    return lista


def lista_nombres():
    dic = {}
    f = open('Score.txt', 'r')
    linea = f.readline()
    while linea != '':   #Con bucle while es más eficiente
        linea = linea.strip('\n')
        linea = linea.split()
        puntos.append(linea)
        dic[int(linea[1])] = linea[0]
        linea = f.readline()
    return(list(dic.values()))



class Titulo:
    def __init__(self):
        turtle.Turtle.__init__
        self = turtle.Turtle()
        self.up()
        self.pencolor(color)
        self.hideturtle()
        self.setpos(0, 230)
        self.write('RANKING MEJORES JUGADORES', False, align="center", font=("Calibri", 40))
    

class Nombres:
    def __init__(self):
        turtle.Turtle.__init__
        for i in range(5):
            self = turtle.Turtle()
            self.up()
            self.pencolor("white")
            self.hideturtle()
            self.setpos(-100, 100 - 100*i)
            self.write(str(lista_nombres()[i]), False, align="center", font=("Calibri", 30))

class Puntos(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        for i in range(5):
            self = turtle.Turtle()
            self.up()
            self.pencolor("yellow")
            self.hideturtle()
            self.setpos(100, 100 - 100*i)
            self.write(str(lista_puntuaciones()[i]), False, align="center", font=("Arial", 30))

    
class Boton:
    def __init__(self):
        self = turtle.Turtle()
        self.up()
        self.shape(volver)
        self.speed("fastest")
        self.setpos(400, -380)

    def boton1(self, x, y):
        pantalla.clearscreen()
        import menu
        

        

t = Titulo()      
n = Nombres()
p = Puntos()
b = Boton()
pantalla.onclick(b.boton1)


pantalla.mainloop()

'''
t.write(str(linea), False, align="center", font=("Arial", 30))
'''
