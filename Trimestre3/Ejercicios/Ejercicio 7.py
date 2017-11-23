"""
    Crear una tabla para la clase Contacto y gestionar la agenda.
    Ha de contener métodos para
        insertar contactos
        Agenda - 'cargar_contacto' a través de su identificador
        Agenda - 'cargar_contacto' a través de su nombre
        Agenda - 'cargar_agenda' que lea todos los contactos
        Agenda - 'nuevo_contacto' que cree y guarde un contacto nuevo
    Detectar errores
        qué error produce cuando se pide un identificador no existente
"""

import sqlite3

class Contacto:
    def __init__(self,nombre,edad,telefono,email):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.email = email

class Agenda():
    def __init__(self,contactos):
        self.contactos = contactos
        self.i = 0

    def meter(self, contacto):
        '''Introduce un contacto en la agenda'''
        self.contactos[contacto.nombre] = contacto
    
    def obtener_contactos(self, nombre):
        '''Devuelve el elemento del diccionario que corresponda con el nombre'''
        return self.contactos[nombre]
    
    
def anadir_contacto(contacto):
    try:
        c.execute('INSERT INTO contacto VALUES("{}",{},"{}","{}");'.format(contacto.nombre,contacto.edad,contacto.telefono,contacto.email))
        conn.commit()
    except Exception as error: #Con Exception capturamos cualquier excepcion posible
        print('Error producido: ',error)
        
def ver_contacto(nombre_contacto):
    res = c.execute('SELECT * FROM contacto WHERE contacto.nombre = ?',(nombre_contacto,))
    return res.fetchall()

def cargar_agenda():
    agenda = []
    agenda.append(c.execute('''SELECT * FROM contacto'''))


try:
    conn = sqlite3.connect('agenda.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS contacto')
    cadena_sql = '''CREATE TABLE contacto(nombre TEXT, edad INT, telefono INT, email TEXT)'''
    c.execute(cadena_sql)
    conn.commit() #Guarda los cambios que se realizan sobre la base de datos

except Exception as error1:
    print('Error producido: ',error1)
    
finally:
    pass
    #conn.close()

c1 = Contacto('Antonio',20,'55634523','antonio@gmail.com')
c2 = Contacto('Juan',14,'43423423','juan@gmail.com')
c3 = Contacto('Pepito',17,'4234234','pepe@gmail.com')

anadir_contacto(c1)
anadir_contacto(c2)
anadir_contacto(c3)

print(ver_contacto('Antonio'))
