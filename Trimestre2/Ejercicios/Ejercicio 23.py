from random import randint

fichero = open('nombres.txt')

class Persona:
    def __init__(self, nom, eda):
        self.nombre = nom
        self.edad = eda
    def __str__(self):
        return 'Persona({},{})'.format(self.nombre, self.edad)

lista = []

for i in fichero:
    lista.append(Persona(i, randint(1, 100)))
for j in lista:
    print(j)

    
#Otra forma, con lista por comprensión
'''
familia = [ Persona(i, randint(1,100)) for i in fichero]
for i in familia:
    print(i)
'''
