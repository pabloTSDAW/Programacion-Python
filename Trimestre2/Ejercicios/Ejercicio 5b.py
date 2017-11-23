import turtle
s = turtle.Screen()


#Apartado b

mario = turtle.Turtle()
mario.speed('slow')
mario.shape('square')
luigi = mario.clone()
mario.pen(pencolor='red', fillcolor='red')
luigi.pen(pencolor='green', fillcolor='green')


mario.up()
luigi.up()

luigi.setpos(300,0)
mario.setpos(-300,0)


def choques(num):
    """Hace que Mario y Luigi choquen y ambos cambien de color"""
    for i in range(num):
        while mario.distance(luigi) > 20:
            mario.fd(10)
            luigi.back(10)
        mario.fillcolor('coral1')
        luigi.fillcolor('PaleGreen2')
        while mario.distance(luigi) != 600:
            mario.back(10)
            luigi.fd(10)
        mario.fillcolor('red')
        luigi.fillcolor('green')

choques(20)


