from math import sqrt
from math import hypot

class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self): #Da la visión gráfica de un objeto Punto en un str
        return 'Punto({},{})'.format(self.x, self.y)
    
    def __eq__(self, otro):
        '''Nos dice si un punto es igual a otro'''
        return self.x == otro.x and self.y == otro.y
    
    def __le__(self, otro):
        '''Nos dice si un punto es menor o igual que otro'''
        return sqrt(self.x**2 + self.y**2) <= sqrt(otro.x**2 + otro.y**2)

    def __lt__(self, otro):
        '''NOs dice si un punto es menor que otro'''
        return sqrt(self.x**2 + self.y**2) < sqrt(otro.x**2 + otro.y**2)

    def __ge__(self, otro):
        '''Nos dice si un punto es mayor o igual que otro'''
        return sqrt(self.x**2 + self.y**2) >= sqrt(otro.x**2 + otro.y**2)

    def __gt__(self, otro):
        '''Nos dice si un punto es mayor que otro'''
        return sqrt(self.x**2 + self.y**2) > sqrt(otro.x**2 + otro.y**2)
    
    def __add__(self, otro):
        '''A un punto le suma otro'''
        return (self.x + otro.x, self.y + otro.y)
    
    def __sub__(selfself, otro):
        '''A un punto le resta otro'''
        return (self.x - otro.x, self.y - otro.y)
    
    def __abs__(self):
        '''Nos da el valor absoluto de un número'''
        return hypot(self.x, self.y)
    

p = Punto(100,50)
q = Punto(120,200)
o = Punto(120,200)

print(o.__eq__(q))
print(o.__gt__(q))
print(p.__add__(o))
print(p.__abs__())
