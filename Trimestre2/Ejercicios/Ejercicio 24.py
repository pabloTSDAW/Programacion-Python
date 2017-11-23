
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pareja = None
        
    def __str__(self):
        return 'Persona({},{},{})'.format(self.nombre, self.edad, self.pareja.nombre)
    
    def presentate(self):
        '''Hace que la persona se presente'''
        if self.pareja != None:
            return 'Hola, me llamo {}, tengo {} años y mi pareja se llama {}.'.format(self.nombre, self.edad, self.pareja.nombre)
        else:
            return 'Hola, me llamo {}, tengo {} años y estoy más solo que la una.'.format(self.nombre, self.edad)

    def emparejar(self, persona):
        '''Empareja a persona con otra persona'''
        self.pareja = persona
        self.liberar(persona)
        persona.pareja = self
        
    def desemparejar(self, persona):
        '''Desempareja a persona de otra pareja'''
        self.pareja = None
        persona.pareja = None

    def liberar(self, persona):
        persona.pareja = None
        

x = Persona('Pablo', 31)
y = Persona('Pepe', 30)
z = Persona('Juana', 25)

#Resultado
'''
y.presentate()
Hola, me llamo Pepe, tengo 30 años y mi pareja se llama None.
>>> y.emparejar(z)
>>> y.presentate()
Hola, me llamo Pepe, tengo 30 años y mi pareja se llama Juana.
>>> y.desemparejar(y)
>>> y.presentate()
Hola, me llamo Pepe, tengo 30 años y mi pareja se llama None.
'''
