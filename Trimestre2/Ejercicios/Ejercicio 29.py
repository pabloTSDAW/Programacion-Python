'''Construir una clase derivada que tenga dos clases bases y
comprobar el orden de resolución de un método. (class Derivada(Base1, Base2)
Realizar lo mismo con tres niveles (Padre, Hijo1, Hijo2, Nieto). Para ello:
Vamos a definir la clase mascota (animal con nombre) y perro doméstico
(perro y mascota).'''

class Animal:
    def __init__(self, moviendo = False):
        self.moviendo = moviendo

    def __str__(self): #Da la visión gráfica de un objeto Animal en un str
        return 'Animal({})'.format(self.moviendo)

    def parar(self):
        self.moviendo = False

    def mover(self):
        self.moviendo = True
        

class Perro(Animal):
    '''Animal'''
    def __init__(self):
        Animal.__init__(self, moviendo = False)

    def ladra(self):
        print('Guau')


class Mascota(Animal):
    '''Animal'''
    def __init__(self):
        Animal.__init__(self, moviendo = False)

    def nombre(self, nom):
        self.nom = nom
        return 'Mascota({}, {})'.format(self.nom, self.moviendo)


class Perro_domestico(Perro, Mascota):
    '''Perro y Mascota'''
    def __init__(self):
        Perro.__init__(self)
        Mascota.__init__(self)

a = Animal()
b = Mascota()
c = Perro()
d = Perro_domestico()
        


