''' ----------------------------------------------------------------- '''
''' PROYECTO PROGRAMACIÓN - ACCESO A BASE DE DATOS E INTERFAZ GRÁFICO '''
''' ----------------------------------------------------------------- '''

import mysql.connector
from tkinter import *


'''PRODUCTO'''

class Producto:
    def __init__(self, ref, nombre, descripcion, precioUnidad, tipo, unidades):
        self.ref = ref
        self.nombre = nombre
        self.descripcion = descripcion
        self.precioUnidad = precioUnidad
        self.tipo = tipo
        self.unidades = unidades

    def __str__(self):
        return 'Producto({},{},{},{},{},{})'.format(self.ref, self.nombre, self.descripcion,\
                                                    self.precioUnidad, self.tipo, self.unidades)


'''COLECCIÓN DE PRODUCTOS'''

class ColeccionProductos:
    def __init__(self):
        self.dic_productos = {}
        self.bd = ControlBD()
        self.bd.conectar()

    def generador(self):
        '''Genera números de referencia para los productos'''
        self.bd.referencias()
        num = int(self.bd.c.fetchone()[0])
        while True:
            yield num + 1
            num += 1

    def obtener_producto(self, ref):
        '''Devuelve el producto a partir de un numero de referencia'''
        try:
            self.bd.obtener_productoBD(ref)
            datos = self.bd.c.fetchone()
            ref, nombre, descripcion, precioUnidad, tipo, unidades = datos
            return Producto(ref, nombre, descripcion, precioUnidad, tipo, unidades)
        except Exception as error:
            print(error)
        
    def ver_productos(self):
        '''Muestra todos lo productos'''
        try:
            self.bd.ver_productosBD()
            for row in self.bd.c:
                ref, nombre, descripcion, precioUnidad, tipo, unidades = row
                self.dic_productos[ref] = nombre, descripcion, precioUnidad, tipo, unidades
            return self.dic_productos
        except Exception as error:
                print(error)
    
    def introducir_producto(self, nombre, descripcion, precioUnidad, tipo, unidades):
        '''Inserta un nuevo registro en la tabla producto'''
        a = self.generador()
        ref = next(a)
        try:
            producto = Producto(ref, nombre, descripcion, precioUnidad, tipo, unidades)
            self.bd.introducir_productoBD(producto)
            self.bd.conexion.commit()
        except Exception as error:
            print(error)


        

'''CONEXIÓN CON BASE DE DATOS'''

class ControlBD:
    def __init__(self):
        self.conexion = None
        self.c = None

    def conectar(self):
        '''Conecta con la base de datos'''
        cnx = mysql.connector.connect(user='root',
                              password='654321', host='localhost',
                              database='proyecto')
        self.conexion = cnx
        self.c = cnx.cursor()

    def ver_tablas(self):
        '''Muestra las tablas existentes en el proyecto'''
        return self.c.execute("SHOW TABLES")

    def referencias(self):
        '''Busca el numero de referencia más alto'''
        return self.c.execute("SELECT ref FROM producto ORDER BY ref DESC LIMIT 1")

    def obtener_productoBD(self, ref):
        '''Devuelve el producto a partir de un numero de referencia'''
        return self.c.execute("SELECT * FROM producto WHERE ref = {}".format(ref))

    def ver_productosBD(self):
        '''Muestra todos lo productos'''
        return self.c.execute("SELECT * FROM producto")

    def introducir_productoBD(self, producto):
        '''Inserta un nuevo registro en la tabla producto'''
        try:
            query = "INSERT INTO producto VALUES({},'{}','{}',{},'{}',{})".format(producto.ref, producto.nombre, producto.descripcion, producto.precioUnidad, producto.tipo, producto.unidades)
            return self.c.execute(query)
            self.conexion.commit()
        except Exception as error:
            print(error)




class Ventana(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = 'white')
        self.parent = parent
        self.color = 'lightgreen'
        self.Igrafico()         #siempre al final del init
        

    def Igrafico(self):
        '''Interfaz Gráfico'''
        self.parent.title('PRINCIPAL')
        self.grid()

        self.titulo = Label(self, text='¿QUÉ DESEA HACER?', width=38, background='gray29', fg='white')
        self.titulo.grid(row=1, column=1, columnspan = 2)
        
        self.insertar = Button(self, width = 38, text = 'INSERTAR', command = self.insertar, background = 'sandy brown')
        self.insertar.grid(row=2, column=2)

        self.producto = Button(self, width = 38, text = 'BUSCAR PRODUCTO', command = self.buscar_productos, background = 'sandy brown')
        self.producto.grid(row=4, column=2)

        self.productos = Button(self, width = 38, text = 'VER PRODUCTOS', command = self.ver_productos, background = 'sandy brown')
        self.productos.grid(row=6, column=2)
        

    def insertar(self):
        import insertar

    def buscar_productos(self):
        import obtener

    def ver_productos(self):
        import imprimir
        

    

def importar_coleccion():
    '''Crea la colección'''
    col = ColeccionProductos()
    return col



def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()

if __name__ == '__main__':
    main()
