import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('square')
p = t.clone()
t.shapesize(2,2)
t.pen(fillcolor='green')
t.up()
t.setpos(-200,200)
p.shape('square')

#Apartado d

def cambiacolor(x,y):
    """Cambia la tortuga de color"""
    if t.fillcolor() == 'red':
        t.fillcolor('green')
        p.down()
    else:
        t.fillcolor('red')
        p.up()
        
t.onclick(cambiacolor, 3) #el 3 es el botón derecho del ratón       
    

def salta(x,y):
    """Hace que la tortuga salte a donde pinchas con el ratón"""
    p.goto(x,y)

s.onclick(salta)


s.mainloop() #Hay que ponerlo siempre al final
