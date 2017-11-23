'''a) Crear un conversor de temperaturas. Sin boton, con eventos
b) Cuando alguna de las cajas gane el foco, se limpian las
dos cajas automáticamente.'''


from tkinter import *

class Ventana(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = 'white')
        self.parent = parent
        self.color = 'lightgreen'
        self.faren = 0
        self.celsius = 0
        self.var = IntVar()
        self.Igrafico()         #siempre al final del init


    def Igrafico(self):
        '''Interfaz Gráfico'''
        self.parent.title('Ejercicio 4')
        self.grid()

        self.entrada = Entry(self, textvariable = self.var, justify = "center")
        self.entrada.grid(row=1, column=3)
                             
        self.entrada.bind("<Return>", self.f_a_c)

        self.texto1 = Label(self, text = '{}'.format(self.celsius), background = "white")
        self.texto1.grid(row=3, column=2, columnspan=2)

        self.texto2 = Label(self, text = 'Celsius:', width = 20)
        self.texto2.grid(row=3, column=1)

        self.texto3 = Label(self, text = 'Farenheit: ', width = 20)
        self.texto3.grid(row=1, column=1)
                             
        
    def f_a_c(self, Return):
        '''Convierte de Farenheit a Celsius'''
        self.entrada.focus_set()
        self.faren = self.var.get()
        self.celsius = round((self.faren - 32)*5/9,2)
        self.texto1['text'] = '{}'.format(self.celsius)


    def c_a_f(self, Return):
        '''Convierte de Farenheit a Celsius'''
        self.entrada.focus_set()
        self.celsius = self.var.get()
        self.faren = round((self.celsuis *9/5) + 32, 2)
        self.texto1['text'] = '{}'.format(self.faren)            


def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()


main()
