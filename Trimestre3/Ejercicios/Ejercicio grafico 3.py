'''a) Crear una tiqueta y un botón. Cuando pulsamos el botón,
la etiqueta va cambiando.
b) Cada vez que cuente, que cambie alternativamente de color.
c) Crear una caja de texto (Entry) dentro del interfaz.'''


from tkinter import Tk, Frame, Button, BOTH, Label

class Ventana(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = 'white')
        self.parent = parent
        self.contador = 0
        self.color = 'lightgreen'
        self.Igrafico()

    def Igrafico(self):
        '''Interfaz Gráfico'''
        self.parent.title('Ejercicio 3')
        self.grid()
        self.texto = Label(self, text = 'cuenta: {}'.format(self.contador), background = self.color)
        self.texto.grid()
        self.boton = Button(self, text = 'Pulsador', command = self.contar, background = 'cyan')
        self.boton.grid()
        self.entrada = Entry(self, 
        

    def contar(self):
        self.contador += 1
        self.texto['text'] = 'cuenta: {}'.format(self.contador)
        if self.contador%2 == 0:
            self.texto['background'] = 'lightgreen'
        else:
            self.texto['background'] = 'yellow'
            


def main():
    root = Tk()
    app = Ventana(root)
    root.mainloop()


main()

        

