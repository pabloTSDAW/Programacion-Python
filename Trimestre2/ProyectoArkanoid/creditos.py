import turtle
from random import randint

pantalla = turtle.Screen()
pantalla.screensize(400, 300)
pantalla.setup(width=1000, height=800, startx=270, starty=0)
pantalla.bgcolor("black")

t = turtle.Turtle()
t.up()
t.pencolor("yellow")
t.hideturtle()
t.goto(0,-60)
t.lt(90)
t.speed("slowest")

def abrir(fichero):
    """Abre el fichero créditos, lo imprime linea a linea por pantalla
    y captura los posibles errores"""
    prueba = True
    while prueba:
        try:
            f = open(fichero, 'r')
            linea = f.readline()
            while linea != '':   #Con bucle while es más eficiente
                print(linea)
                t.write(str(linea), False, align="center", font=("Arial", 30))
                t.fd(450)
                t.clear()
                t.goto(0,-60)
                linea = f.readline()
        except FileNotFoundError as error1:
            print('Fichero no encontrado')
        else:
            prueba = False
    pantalla.clearscreen()
    import menu

               
abrir("creditos.txt")


pantalla.mainloop()
