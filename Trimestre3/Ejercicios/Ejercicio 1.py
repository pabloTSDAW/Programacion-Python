'''Hacer que la Agenda (clase del trimestre pasado)
verifique el protocolo iterable. '''

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return '({},{},{})'.format(self.nombre, self.telefono, self.email)

class Agenda:
    def __init__(self, contactos):
        self.contactos = contactos
        self.i = 0

    def meter(self, contacto):
        '''Introduce un contacto en la agenda'''
        self.contactos[contacto.nombre] = contacto
        
    def carga_contactos(self, fichero):
        '''Carga los contactos desde el fichero contactos.txt'''
        self.fichero = fichero
        f = open(fichero)
        texto = f.readlines()
        for i in texto:
            dato = i.split(',')
            contacto = Contacto(dato[0], dato[1], dato[2])
            self.meter(contacto)

    def __next__(self):
        '''Devuelve el siguiente elemento de la agenda'''
        nombres = list(self.contactos.keys())
        nombres.sort()
        valores = list(self.contactos.values())
        dic = {}
        if self.i < len(nombres):
            n = self.i
            self.i += 1
            dic[nombres[n]] = valores[n]
            return dic
        else:
            raise StopIteration

    def __iter__(self):
        return self

    def obtener_contactos(self, nombre):
        '''Devuelve el elemento del diccionario que corresponda con el nombre'''
        return self.contactos[nombre]
    
telefonos = {}

a = Agenda(telefonos)


p = Contacto('pablo', '661155196', 'p@gmail.com')
c = Contacto('carlos', '661155193', 'c@gmail.com')
t = Contacto('tomy', '678075731', 't@gmail.com')

a.meter(p)
a.meter(c)
a.meter(t)
    
print(a.obtener_contactos('pablo'))  
