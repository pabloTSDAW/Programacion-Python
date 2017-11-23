''' Definir la clase Animal, puede estar moviéndose o no (boolean),
y va a tener un método mover y uno parar. Este método cambia el estado
de movimiento del animal. Vamos a crear una clase derivada Perro que
va a tener un método ladra (print(guau)).'''

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
    def __init__(self):
        Animal.__init__(self, moviendo = False)

    def ladra(self):
        print('Guau')



a = Animal()
b = Animal()
c = Perro()
        
        
