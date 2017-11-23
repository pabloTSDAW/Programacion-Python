'''Crear una clase Contacto (con nombre y teléfono) y
mantener un contador de personas creadas. Vamos a enumerar
las personas (nombre, teléfono y número creado a partir del
contador). El contador está dentro de la clase. Definir que
variables son de clase y cuales de instancia.'''

class Contacto:
    contador = 0
    
    def __init__(self, nombre, telefono):
        Contacto.contador += 1
        self.numero = Contacto.contador
        self.nombre = nombre
        self.telefono = telefono
        


a = Contacto('Pablo', 4321)
b = Contacto('Carlos', 1234)
c = Contacto('Tomy', 1111)
d = Contacto('Lorena', 4444)

print(a.__dict__)   #a.__dict__  nos muestra todos los atributos de a
print(b.__dict__)
print(c.__dict__)
print(d.__dict__)

