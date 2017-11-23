class Persona:
    def __init__(self, nom, eda):
        self.nombre = nom
        self.edad = eda
    def __str__(self):
        return 'Persona({},{})'.format(self.nombre, self.edad)


p1 = Persona('Antonio', 62)
p2 = Persona('Carlos', 31)
p3 = Persona('Pablo', 32)

familia = [p1, p2, p3]

for i in familia:
    print(i)


#Otra forma con concatenación

class Persona2:
    def __init__(self, nom, edad):
        self.nombre = nom
        self.edad = edad
    def __str__(self):
        return ('Persona'+'('+self.nombre+','+self.edad+')')

'''
x = Persona2('Pablo', '25')
print(x)
'''

#Apartado b

class Persona:
    def __init__(self, nom, eda):
        self.nombre = nom
        self.edad = eda
    def __str__(self):
        return 'Persona({},{})'.format(self.nombre, self.edad)

lista = []

for i in range(1001):
    lista.append(Persona('Pepe', '25'))
for i in lista:
    print(i)
    
