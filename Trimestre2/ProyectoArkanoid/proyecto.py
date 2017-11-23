import turtle
from random import randint

nave = 'Objetos/nave2.gif'
heart = 'Objetos/heart.gif'
fondo = 'Fondos/sky2.png'
grande = 'Objetos/grande.gif'
pequeño = 'Objetos/pequeño.gif'

corazones = []
ladrillos = []
eliminados = []
paso = 7
desplazamiento = 30

vidas = 3
giro_inicial = 80

#Cuadrantes angulos
c1 = range(1, 90)
c2 = range(91, 180)
c3= range(181, 270)
c4 = range(271, 360)

#Pantalla
pantalla = turtle.Screen()
pantalla.title("WELCOME TO ARKANOID!!!")
pantalla.screensize(400, 300)
pantalla.bgpic(fondo)
pantalla.register_shape(nave)
pantalla.register_shape(heart)
pantalla.register_shape(grande)
pantalla.register_shape(pequeño)
pantalla.setup(width=1000, height=800, startx=270, starty=0)


#Velocidades - Tracer pantalla
def speed2():
    '''Aumenta la velocidad de dibujo'''
    pantalla.tracer(False)

def speed1():
    '''Retorna la velocidad de dibujo a su estado normal'''
    pantalla.tracer(1)


#Pantalla de juego
class Entorno:
    def dibuja_campo(self):
        '''Dibuja los límites del escenario principal'''
        m = turtle.Turtle()
        m.shape('square')
        m.pen(fillcolor="blue")
        m.pencolor('grey')
        m.pensize(5)
        m.speed('fastest')
        m.hideturtle()
        m.up()
        m.goto(400,300)
        m.down()
        m.goto(400, 300)
        m.pencolor("red")
        m.goto(-400,-300)
        m.pencolor("grey")
        m.goto(-400,300)
        m.goto(400,300)


#bloques enemigos
posiciones1 = [(x, y) for x in range(-320, 321, 80) for y in range(180, 241, 20)]
posiciones2 = [(x, y) for x in range(-320, 321, 120) for y in range(120, 241, 20)]

colores = [('grey'), ('cyan'), ('greenyellow'), ('orange'), ('purple')]       

ladrillos = []


#Clase Bloque
class Bloque(turtle.Turtle):
    def __init__(self, posicion, color):
        turtle.Turtle.__init__(self)
        self.up()
        self.shapesize(1,4)
        self.shape("square")
        self.posicion = posicion
        self.setpos(posicion)
        self.color = color
        self.fillcolor(color)
        
        
def crea_bloques():
    '''Construye bloques en las posiciones de la lista posiciones'''
    speed2()
    for i in posiciones1:
        bloque = Bloque(i, colores[randint(0, len(colores)-1)])
        ladrillos.append(bloque)
    speed1()


def elimina_bloque(bloque):
    '''Elimina un bloque y lo elimina de la lista ladrillos'''
    speed2()
    bloque.hideturtle()
    bloque.goto(400,300)
    ladrillos.remove(bloque)
    speed1()



#Clase Jugador
class Jugador(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.up()
        self.setpos(0,-250)
        self.shape(nave)
        self.shapesize(1,4)
        self.fillcolor("white")

    def derecha(self):
        '''Mueve al jugador hacia la derecha'''
        if self.xcor() <= 340:
            speed2()
            self.fd(desplazamiento)
            speed1()

    def izquierda(self):
        '''Mueve al jugador a la izquierda'''
        if self.xcor() >= -340:
            speed2()
            self.back(desplazamiento)
            speed1()



#Clase Vidas
class Vidas(turtle.Turtle):
    def __init__(self, numero):
        turtle.Turtle.__init__(self)
        self.numero = numero
        for i in range(numero):
            self = turtle.Turtle()
            self.up()
            self.speed("fastest")
            self.setpos(350 - 50*i, 360)
            self.shape(heart)
            corazones.append(self)


"""PROXIMAMENTE - Implementar en futuras revisiones"""

"""
#Clase Extras
class Extras(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.up()
        self.speed("fastest")
        self.hideturtle()           

    def aparece_extra(self):
        '''Muestra el extra en la pantalla de juego'''
        self.showturtle()
        self.setpos(randint(-380, -50), -250)

    def borra_extra(self):
        '''Elimina el extra de la pantalla de juego'''
        self.hideturtle()
        self.goto(-400,400)



#Clase Extra - Grande
class Grande(Extras):
    def __init__(self):
        Extras.__init__(self)
        self.shape(grande)
        self.setpos(randint(50, 380), -250)
        

#Clase Extra - Pequeño
class Pequeño(Extras):
    def __init__(self):
        Extras.__init__(self)
        self.shape(pequeño)
        self.setpos(randint(50, 380), -250)
"""    
                   
        
#Clase Puntuación
class Puntuacion(turtle.Turtle):
    def __init__(self, color, puntos):
        turtle.Turtle.__init__(self)
        self.puntos = puntos
        self.color = color
        self.up()
        self.pencolor(color)
        self.hideturtle()
        self.setpos(-350, 305)
        self.write(str(puntos), False, align="center", font=("Arial", 30))
        
    def suma_puntos(self, puntos):
        '''Añade 50 puntos'''
        self.clear()
        self.write(str(puntos), False, align="center", font=("Arial", 30))

    def resta_puntos(self, puntos):
        '''Resta 100 puntos'''
        self.clear()
        self.write(str(puntos), False, align="center", font=("Arial", 30))
        

def guardar(puntos):
    '''Guarda la puntuación en un fichero de texto'''
    nombre = pantalla.textinput("Puntuación: " + str(puntos), "Nombre")
    if nombre == '' or ' ' in nombre:
        raise NameError('Introduce un nombre válido (sin espacios)')
    else:
        f = open('Score.txt', 'a')
        f.write(str(nombre) + ' ' + str(puntos) + '\n')
        f.close()
        pantalla.bye()


    
#Clase Pelota
class Pelota(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.up()
        self.shape("circle")
        self.setpos(0, -230)
        self.fillcolor("light gray")
        self.speed("fastest")
        self.setheading(giro_inicial)
        
        
    #Ángulos de rebote
        #Con los límites del campo
    def rebote_y_pos1(self):
        speed2()
        self.right(self.heading() * 2)
        self.fd(5)
        speed1()

    def rebote_y_pos2(self):
        speed2()
        self.left((180 - self.heading())*2)
        self.fd(5)
        speed1()

    def rebote_x_pos1(self):
        speed2()
        self.left((90 - self.heading()) * 2)
        self.fd(5)
        speed1()

    def rebote_x_pos2(self):
        speed2()
        self.right((90 - (360 - self.heading())) * 2)
        self.fd(5)
        speed1()

    def rebote_x_neg1(self):
        speed2()
        self.right((self.heading() - 90) * 2)
        self.fd(5)
        speed1()

    def rebote_x_neg2(self):
        speed2()
        self.left((270 - self.heading()) * 2)
        self.fd(5)
        speed1()

    def limite_superior(self):
        return self.ycor() >= 287

    def limite_derecho(self):
        return self.xcor() >= 390

    def limite_izquierdo(self):
        return self.xcor() <= -390

    def rebotes_limites(self):
        '''Permite que la pelota rebote con los límites del campo'''
        if self.limite_superior() and self.cuadrante1():
            self.rebote_y_pos1()
        if self.limite_superior() and self.cuadrante2():
            self.rebote_y_pos2()
        if self.limite_derecho() and self.cuadrante1():
            self.rebote_x_pos1()
        if self.limite_derecho() and self.cuadrante4():
            self.rebote_x_pos2()
        if self.limite_izquierdo() and self.cuadrante2():
            self.rebote_x_neg1()
        if self.limite_izquierdo() and self.cuadrante3():
            self.rebote_x_neg2()

        #Con el jugador
    def rebote_jug1(self):
        speed2()
        self.right(self.heading() * 2)
        self.fd(5)
        speed1()

    def rebote_jug2(self):
        speed2()
        self.left((360 - self.heading()) * 2)
        self.fd(5)
        speed1()

    def rebote_jug3(self):
        speed2()
        self.right(randint(170, 190))
        self.fd(5)
        speed1()

    def rebote_jug4(self):
        speed2()
        self.left(randint(170, 190))
        self.fd(5)
        speed1()

    def limite_jugador1(self, jugador):
        return jugador.xcor() - 50 <= self.xcor() <= jugador.xcor() and jugador.ycor() - 20 <= self.ycor() <= jugador.ycor() + 20

    def limite_jugador2(self, jugador):
        return jugador.xcor() +1 <= self.xcor() <= jugador.xcor() + 50 and jugador.ycor() - 20 <= self.ycor() <= jugador.ycor() + 20

        #Cuadrantes de ángulos de rebote
    def cuadrante1(self):
        return self.heading() in c1

    def cuadrante2(self):
        return self.heading() in c2

    def cuadrante3(self):
        return self.heading() in c3

    def cuadrante4(self):
        return self.heading() in c4

        #Con los bloques
    def rebote_bloque_horizontal(self, bloque):
        return bloque.xcor() - 45 <= self.xcor() <= bloque.xcor() + 45 and bloque.ycor() - 23 <= self.ycor() <= bloque.ycor() + 23

    def rebote_bloque_vertical(self, bloque):
        return bloque.xcor() - 48 <= self.xcor() <= bloque.xcor() + 48 and bloque.ycor() + 23 >= self.ycor() >= bloque.ycor() - 23


        

#Clase Partida
class Partida:
    def __init__(self):
        e = Entorno()
        e.dibuja_campo()
        crea_bloques()
        self.v = Vidas(vidas)
        self.p = Pelota()
        self.j = Jugador()
        puntos = 0
        self.pun = Puntuacion("gold", puntos)


    def reinicia(self):
        '''Reinicia la posición de la pelota y del jugador'''
        self.p.hideturtle()
        self.p.goto(0,-230)
        self.p.setheading(100)
        self.p.showturtle()
        fuera = corazones.pop()
        fuera.hideturtle()
        self.j.setpos(0, -250)
        

    def unomenos(self, enemigo, punt):
        '''Elimina un bloque y suma 50 puntos al marcador'''
        elimina_bloque(enemigo)
        self.pun.suma_puntos(punt)


    def fin(self):
        '''Termina la partida cuando se acaban las vidas'''
        if corazones == []:
            self.game_over()
            try:
                guardar(puntos)
            except NameError as error1:
                print(error1)
    

    def rebotes_jugador(self):
        '''Permite que la pelota rebote con el jugador'''
        if self.p.limite_jugador1(self.j) and self.p.cuadrante3():
            self.p.rebote_jug1()
        if self.p.limite_jugador2(self.j) and self.p.cuadrante4():
            self.p.rebote_jug2()
        if self.p.limite_jugador2(self.j) and self.p.cuadrante3():
            self.p.rebote_jug3()
        if self.p.limite_jugador1(self.j) and self.p.cuadrante4():
            self.p.rebote_jug4()
            

    def game_over(self):
        '''Escribe GAME OVER cuando termina la partida'''
        self.p.goto(0,0)
        self.p.hideturtle()
        self.p.pencolor("red")
        self.p.write("GAME OVER", False, align="center", font=("Arial", 30))
        self.j.hideturtle()


    def you_win(self):
        '''Escribe VICTORIA cuando termina la partida'''
        self.p.goto(0,0)
        self.p.hideturtle()
        self.p.pencolor("gold")
        self.p.write("¡¡¡¡ VICTORIA !!!!", False, align="center", font=("Arial", 30))
        self.j.hideturtle()
        
    
    def iniciar(self):
        '''Comienza el movimiento de la pelota'''
        puntos = 0
        while True:
            self.p.fd(paso)
            self.rebotes_jugador()
            self.p.rebotes_limites()

            for bloque in ladrillos:
                #Rebote con los bloques, ejes horizontales
                if self.p.rebote_bloque_horizontal(bloque) and self.p.cuadrante1():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_y_pos1()
                if self.p.rebote_bloque_horizontal(bloque) and self.p.cuadrante2():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_y_pos2()
                if self.p.rebote_bloque_horizontal(bloque) and self.p.cuadrante3():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_y_pos1()
                if self.p.rebote_bloque_horizontal(bloque) and self.p.cuadrante4():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_jug2()
                #Rebote con los bloques, ejes verticales
                if self.p.rebote_bloque_vertical(bloque) and self.p.cuadrante1():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_x_pos1()
                if self.p.rebote_bloque_vertical(bloque) and self.p.cuadrante2():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_x_neg1()
                if self.p.rebote_bloque_vertical(bloque) and self.p.cuadrante3():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_x_neg2()
                if self.p.rebote_bloque_vertical(bloque) and self.p.cuadrante4():
                    puntos += 50
                    self.unomenos(bloque, puntos)
                    self.p.rebote_x_pos2()
                    
                #Muerte: cuando la pelota supera el limite inferior
                if self.p.ycor() <= -300:
                    self.reinicia()
                    puntos = puntos - 100
                    self.pun.resta_puntos(puntos)

                #Game over: se acaban las vidas
                if corazones == []:
                    self.game_over()
                    try:
                        guardar(puntos)
                    except NameError as error1:
                        print(error1)

                #Victoria: se eliminan todos los ladrillos
                if len(ladrillos) == 0:
                    self.you_win()
                    try:
                        guardar(puntos)
                    except NameError as error1:
                        print(error1)
        


def principal():
    '''Inicializa la clase Partida'''
    partida = Partida()
    pantalla.onkeypress(partida.j.derecha, 'Right')
    pantalla.onkeypress(partida.j.izquierda, 'Left')
    pantalla.onkey(partida.iniciar, "Up")
    pantalla.listen()

principal()
pantalla.mainloop() 

