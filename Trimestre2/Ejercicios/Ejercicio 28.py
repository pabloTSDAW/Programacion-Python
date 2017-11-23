'''Definir la clase Forma. Va a tener los métodos área y
perímetro. Crear las clases derivadas Circulo (con atributo radio)
y Rectangulo (atributos: base y altura) y Cuadrado (una Derivada de
Rectangulo, con atributo lado que coincide con base y altura).
Definir en cada clase los métodos área y perímetro, en Forma
estarán como pass. Def área(self): pass.'''

class Forma:   
    def area(self):
        return None

    def perimtero(self):
        return None
    

class Circulo(Forma):
    def __init__(self, radio):
        Forma.__init__(self)
        self.area = round(3.14 * radio ** 2, 2)
        self.perimetro = round(2 * 3.14 * radio, 2)

    def __str__(self):
        return 'Forma(area: {} unidades cuadradas, perimetro: {} unidades)'.format(self.area, self.perimetro)

    
class Rectangulo(Forma):
    def __init__(self, base, altura):
        Forma.__init__(self)
        self.area = round(base * altura, 2)
        self.perimetro = round(2 * base + 2 * altura, 2)

    def __str__(self):
        return 'Forma(area: {} unidades cuadradas, perimetro: {} unidades)'.format(self.area, self.perimetro)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        Rectangulo.__init__(self, lado, lado)

    def __str__(self):
        return 'Forma(area: {} unidades cuadradas, perimetro: {} unidades)'.format(self.area, self.perimetro)
    
    
a = Circulo(5)
b = Rectangulo(5,3)
c = Cuadrado(5)
        
