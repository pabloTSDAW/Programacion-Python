import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('square')

#Apartado b

def salta(x,y):
    """Hace que la tortuga salte a donde pinchas con el ratón"""
    t.goto(x,y)

s.onclick(salta) #onclick de la pantalla

s.mainloop() #Hay que ponerlo siempre al final


    
