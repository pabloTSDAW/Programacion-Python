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
        
        self.nombre = ''
        self.descripcion = ''
        self.precio = 0.0
        self.tipo = ''
        self.unidades = 0
        self.mensaje = ''
        
        self.ref = IntVar()
        self.col = ColeccionProductos()
        self.Igrafico()         #siempre al final del init
        

    def Igrafico(self):
        '''Interfaz Gráfico'''
        self.parent.title('PRODUCTOS')
        self.grid()

        self.titulo = Label(self, text='OBTENER PRODUCTO', width=115, background='gray29', fg='white')
        self.titulo.grid(row=1, column=1, columnspan = 6)
            
        self.tref = Label(self, text='Referencia', width=10, background="SteelBlue3", fg='white')
        self.tref.grid(row=2, column=1)
        self.eref = Entry(self, textvariable = self.ref, justify="center", background = 'sandy brown', width=10)
        self.eref.grid(row=3, column=1)
        self.eref.bind("<Return>", self.obtener)
        

        self.tnombre = Label(self, text='Nombre', width=20, background="SteelBlue3", fg='white')
        self.tnombre.grid(row=2, column=2)
        self.enombre = Label(self, text = '{}'.format(self.nombre), justify="center", background = 'white')
        self.enombre.grid(row=3, column=2)

        self.tdescripcion = Label(self, text='Descripcion', width=20, background="SteelBlue1", fg='white')
        self.tdescripcion.grid(row=2, column=3)
        self.edescripcion = Label(self, text = '{}'.format(self.descripcion), justify="center", background = 'white')
        self.edescripcion.grid(row=3, column=3)

        self.tprecio = Label(self, text='Precio', width=20, background="SteelBlue3", fg='white')
        self.tprecio.grid(row=2, column=4)
        self.eprecio = Label(self, text = '{}'.format(self.precio), justify="center", background = 'white')
        self.eprecio.grid(row=3, column=4)

        self.ttipo = Label(self, text='Tipo', width=20, background="SteelBlue1", fg='white')
        self.ttipo.grid(row=2, column=5)
        self.etipo = Label(self, text = '{}'.format(self.tipo), justify="center", background = 'white')
        self.etipo.grid(row=3, column=5)

        self.tunidades = Label(self, text='Unidades', width=20, background="SteelBlue3", fg='white')
        self.tunidades.grid(row=2, column=6)
        self.eunidades = Label(self, text = '{}'.format(self.unidades), justify="center", background = 'white')
        self.eunidades.grid(row=3, column=6)

        self.mensaje = Label(self, text = '{}'.format(self.mensaje), justify = "center", width=115, background='gray29', fg='white')
        self.mensaje.grid(row = 4, column = 1, columnspan = 6)


    def obtener(self, Return):
        '''Devuelve un producto dado su numero referencia'''
        try:
            self.eref.focus_set()
            self.ref = self.eref.get()
            producto = self.col.obtener_producto(self.ref)
            self.enombre['text'] = '{}'.format(producto.nombre)
            self.edescripcion['text'] = '{}'.format(producto.descripcion)
            self.eprecio['text'] = '{}'.format(producto.precioUnidad)
            self.etipo['text'] = '{}'.format(producto.tipo)
            self.eunidades['text'] = '{}'.format(producto.unidades)
            self.mensaje['text'] = '{}'.format('Producto encontrado')
        except Exception:
            self.mensaje['text'] = '{}'.format('No se encuentra esa referencia en nuestra base de datos')
            self.enombre['text'] = ''
            self.edescripcion['text'] = ''
            self.eprecio['text'] = 0
            self.etipo['text'] = ''
            self.eunidades['text'] = 0
            
   
    

def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()

main() 
