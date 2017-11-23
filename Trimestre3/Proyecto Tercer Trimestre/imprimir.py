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
        
        self.enviar = Button(self, width = 90, text = 'VER PRODUCTOS', command = self.ver, background='gray29', fg='white')
        self.enviar.grid(row=1, column=1, columnspan=4)
        
        self.datos = Text(self, height = 12)
        self.datos.grid(row=3, column=1)
        
         

    def ver(self):
        '''Ver todos los productos'''
        dic = self.col.ver_productos()
        ref = dic.keys()
        valores = dic.values()
        for producto in dic.keys():
            self.datos.insert(INSERT, str(dic[producto]) + '\n')
            
            
        
    
def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()

main()
