''' ----------------------------------------------------------------- '''
''' PROYECTO PROGRAMACIÓN - ACCESO A BASE DE DATOS E INTERFAZ GRÁFICO '''
''' ----------------------------------------------------------------- '''

import mysql.connector
from tkinter import *
from principal import Producto, ColeccionProductos, ControlBD

'''INTERFAZ GRÁFICO'''

class Ventana(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = 'white')
        self.parent = parent
        self.color = 'lightgreen'
        self.nombre = StringVar()
        self.descripcion = StringVar()
        self.precio = DoubleVar()
        self.tipo = StringVar()
        self.unidades = IntVar()
        self.col = ColeccionProductos()
        self.Igrafico()         #siempre al final del init
        

    def Igrafico(self):
        '''Interfaz Gráfico'''
        self.parent.title('PRODUCTOS')
        self.grid()

        self.titulo = Label(self, text='INGRESAR PRODUCTO', width=38, background='gray29', fg='white')
        self.titulo.grid(row=1, column=1, columnspan = 2)
        
        self.tnombre = Label(self, text='Nombre', width=20, background="SteelBlue3", fg='white')
        self.tnombre.grid(row=2, column=1)
        self.enombre = Entry(self, textvariable = self.nombre, justify="center")
        self.enombre.grid(row=2, column=2)

        self.tdescripcion = Label(self, text='Descripcion', width=20, background="SteelBlue1", fg='white')
        self.tdescripcion.grid(row=3, column=1)
        self.edescripcion = Entry(self, textvariable = self.descripcion, justify="center")
        self.edescripcion.grid(row=3, column=2)

        self.tprecio = Label(self, text='Precio', width=20, background="SteelBlue3", fg='white')
        self.tprecio.grid(row=4, column=1)
        self.eprecio = Entry(self, textvariable = self.precio, justify="center")
        self.eprecio.grid(row=4, column=2)

        self.ttipo = Label(self, text='Tipo', width=20, background="SteelBlue1", fg='white')
        self.ttipo.grid(row=5, column=1)
        self.etipo = Entry(self, textvariable = self.tipo, justify="center")
        self.etipo.grid(row=5, column=2)

        self.tunidades = Label(self, text='Unidades', width=20, background="SteelBlue3", fg='white')
        self.tunidades.grid(row=6, column=1)
        self.eunidades = Entry(self, textvariable = self.unidades, justify="center")
        self.eunidades.grid(row=6, column=2)

        self.enviar = Button(self, width = 38, text = 'INSERTAR', command = self.insertar, background = 'sandy brown')
        self.enviar.grid(row=7, column=1, columnspan=3)

    def insertar(self):
        '''Ingresar un producto nuevo'''
        self.col.introducir_producto(self.nombre.get(), self.descripcion.get(), self.precio.get(), self.tipo.get(), self.unidades.get())
        self.enombre.delete(0, END)
        self.edescripcion.delete(0, END)
        self.eprecio.delete(0, END)
        self.etipo.delete(0, END)
        self.eunidades.delete(0, END)
        
    

def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()

main()
