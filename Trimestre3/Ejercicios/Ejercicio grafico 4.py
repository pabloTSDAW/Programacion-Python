'''a)  Crear un conversor de temperaturas. Crear una caja de texto
 Farenheit [ Entry ]  [ Convertir(Button) ]  [ Celsius(Label) ]'''


from tkinter import Tk, Frame, Button, BOTH, Label, Entry, DoubleVar, StringVar, IntVar

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

        self.entrada = Entry(self, textvariable = self.var)
        self.entrada.grid(row=1, column=3)
                             
        self.boton = Button(self, width = 30, text = 'Covertir', command = self.f_a_c, background = 'cyan')
        self.boton.grid(row=2, column=1, columnspan=3)

        self.texto1 = Label(self, text = '{}'.format(self.celsius))
        self.texto1.grid(row=3, column=2, columnspan=2)

        self.texto2 = Label(self, text = 'Celsius:')
        self.texto2.grid(row=3, column=1)

        self.texto3 = Label(self, text = 'Farenheit: ')
        self.texto3.grid(row=1, column=1)
                             
        
    def f_a_c(self):
        '''Convierte de Farenheit a Celsius'''
        self.faren = self.var.get()
        self.celsius = round((self.faren - 32)*5/9,2)
        self.texto1['text'] = '{}'.format(self.celsius)

            


def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()


main()
