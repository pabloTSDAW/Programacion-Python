class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self): #Da la visión gráfica de un objeto Punto en un str
        return 'Punto({},{})'.format(self.x, self.y)


class Traza:
    def __init__(self, lista = []):
        self.lista = lista

    def __str__(self):
        cad = ''
        for punto in self.lista:
            cad += str(punto)
            return 'Traza([{}])'.format(cad)

    def meter(self, punto):
        '''Introduce un punto en la traza'''
        self.lista.append(punto)

    def __contains__(self, otro):
        '''Nos dice si un punto está contenido en una traza'''
        return otro in self.lista

    def __len__(self):
        '''Nos dice la longitud de la traza'''
        return len(self.lista)


p = Punto(100,50)
q = Punto(120,200)
o = Punto(-200,100)

lista2 = []

r = Traza()

r.meter(p)
r.meter(q)
r.meter(o)




