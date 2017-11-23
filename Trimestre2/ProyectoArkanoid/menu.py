import turtle
from random import randint


s = turtle.Screen()
s.title("MENU")
s.screensize(400,300)
s.bgpic('Fondos/sky.png')
j1 = 'Fondos/arkanoid.gif'
j2 = 'Fondos/chess.gif'
j3 = 'Fondos/comecocos.gif'
arkanoid = 'Menu/arkanoid.gif'
chess = 'Menu/chess.gif'
comecocos = 'Menu/comecocos.gif'
credit = 'Menu/creditos.gif'
ranking = 'Menu/ranking.gif'


s.register_shape(arkanoid)
s.register_shape(chess)
s.register_shape(comecocos)
s.register_shape(credit)
s.register_shape(ranking)
s.register_shape(j1)
s.register_shape(j2)
s.register_shape(j3)


s.setup(width=1000, height=800, startx=270, starty=0)


class Titulo():
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.up()
        self.t.goto(0, 250)
        self.t.pencolor("white")
        self.t.write("COLECCIÓN JUEGOS ARCADE", False, align="center",
                   font=("Times New Roman", 35, "bold"))

class Juegos():
    def __init__(self):
        self.juego = turtle.Turtle()
        self.juego.up()
        self.juego2 = self.juego.clone()
        self.juego3 = self.juego.clone()
        self.juego.goto(-340, 0)
        self.juego.shape(j1)
        self.juego2.shape(j2)
        self.juego3.shape(j3)
        self.juego3.goto(340,0)
        
    
class Opciones():
    def __init__(self):
        self.op1 = turtle.Turtle()
        self.op1.up()
        self.op2 = self.op1.clone()
        self.op3 = self.op1.clone()
        self.op4 = self.op1.clone()
        self.op5 = self.op1.clone()
        self.op1.setpos(-340,140)
        self.op2.setpos(0,140)
        self.op3.setpos(338,140)
        self.op1.shape(arkanoid)
        self.op2.shape(chess)
        self.op3.shape(comecocos)
        self.op4.setpos(0,-340)
        self.op4.shape(credit)
        self.op5.shape(ranking)
        self.op5.setpos(-340, -140)

        self.t1 = turtle.Turtle()
        self.t1.hideturtle()
        self.t1.up()
        self.t1.pencolor("red")

        
    def opcion1(self,x,y):
        s.clearscreen()
        import proyecto
        

    def opcion2(self,x,y):
        s.clearscreen()
        try :
            import chess
        except ImportError:
            self.t1.write('EN CONSTRUCCIÓN, PRÓXIMAMENTE PODRÁS DISFRUTAR DE EL',
                          False, align="center", font=("Arial", 20))

    def opcion3(self,x,y):
        s.clearscreen()
        try :
            import comecocos
        except ImportError:
            self.t1.write('EN CONSTRUCCIÓN, PRÓXIMAMENTE PODRÁS DISFRUTAR DE EL',
                          False, align="center", font=("Arial", 20))
            

    def opcion4(self,x,y):
        s.clearscreen()
        import creditos
        

    def opcion5(self,x,y):
        s.clearscreen()
        import ranking
        

def inicio():
    s.tracer(2)
    t1 = Titulo()
    j = Juegos()
    o = Opciones()
    o.op1.onclick(o.opcion1)
    o.op2.onclick(o.opcion2)
    o.op3.onclick(o.opcion3)
    o.op4.onclick(o.opcion4)
    o.op5.onclick(o.opcion5)
    s.tracer(1)

inicio()
s.mainloop()
