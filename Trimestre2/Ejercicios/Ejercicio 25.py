from math import sqrt

import turtle
s = turtle.Screen()
t = turtle.Turtle()
t.shape('turtle')
t.speed('normal')
t.pen(pencolor='blue', fillcolor='green')

#Apartado a

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self): #Da la visión gráfica de un objeto Punto en un str
        return 'Punto({},{})'.format(self.x, self.y)
    
    def suma(self, otro):
        '''self.x + punto.x = otro.x'''
        coorx = self.x + otro.x
        coory = self.y + otro.y
        return Punto(coorx, coory)

    def resta(self, otro):
        '''self.x + punto.x = otro.x'''
        coorx = self.x - otro.x
        coory = self.y - otro.y
        return Punto(coorx, coory)

    def igual(self, otro):
        '''Nos dice si dos puntos son iguales'''
        return (self.x, self.y) == (otro.x, otro.y)

    #Apartado d
    def distancia(self, otro):
        '''Nos da la distancia entre dos puntos'''
        dis = round(sqrt((otro.x - self.x)**2 + (otro.y - self.y)**2), 2)
        return dis


#Apartado b

class Traza:
    def __init__(self, lista = []):
        self.lista = lista

    def __str__(self):
        cad = ''
        for punto in self.lista:
            cad += str(punto)
            return 'Traza([{}])'.format(cad)

    def igual(self, traza):
        '''Nos dice si dos trazas son iguales (si tienen los mismos puntos)'''
        return self.lista == traza.lista

    def meter(self, punto):
        '''Introduce un punto en la traza'''
        self.lista.append(punto)

    def longitud(self):
        '''Nos da la longitud de la traza'''
        for j in range(len(self.lista)-1):
            lista2.append(self.lista[j].distancia(self.lista[j+1]))
        return sum(lista2)
    
#Apartado e

    def guardar(self, fichero):
        '''Guarda las coordenadas de los puntos de la traza en un acrhivo'''
        f = open(fichero, 'w')
        for i in self.lista:
            f.write(str(i.x) + ',' + str(i.y) + '\n')
        f.close()
        
    def cargar(self, fichero):
        '''Carga en una traza los puntos almacenados en un fichero'''
        f = open(fichero, 'r')
        texto = f.readlines()
        for linea in texto:
            linea2 = linea.strip('\n')
            linea2 = linea2.split(',')
            punto = Punto(linea2[0], linea2[1])
            self.lista.append(punto)
        f.close()

#Apartado f
    def dibuja(self, fichero):
        s.tracer(False)
        '''Dibuja la traza'''
        f = open(fichero, 'r')
        texto = f.readlines()
        for linea in texto:
            linea2 = linea.strip('\n')
            linea2 = linea2.split(',')
            print(linea2)
            t.goto(int(linea2[0]), int(linea2[1]))
        f.close()
        s.update()


#Apartado g
camino = []
r2 = Traza()

def captura(x, y):
    '''Guarda los puntos clic del camino de la tortuga'''
    t.goto(x, y)
    paso = Punto(x,y)
    camino.append(paso)

def para():
    '''Guarda el camino seguido por la toruga en un archivo'''
    t.reset()
    nombre = s.textinput("Guardar", "Archivo")
    f = open(nombre, 'w')
    for i in camino:
        f.write(str(i.x) + ',' + str(i.y) + '\n')
    f.close()
    

s.onclick(captura)#onclick de la pantalla

s.onkey(para, "g") #realiza para() al pulsar
s.listen() #Para que escuche el onkey


s.mainloop() #Hay que ponerlo siempre al final
            

p = Punto(100,50)
q = Punto(120,200)
o = Punto(-200,100)
m = Punto(-200,-200)
n = Punto(0,-100)

lista2 = []

r = Traza()
r1 = Traza()

r.meter(p)
r.meter(q)
r.meter(o)
r.meter(m)
r.meter(n)

r.guardar('puntos.csv')

r1.cargar('puntos.csv')

"""r1.dibuja('puntos.csv')"""





        





    
        
