'''Crear un botón entre dos etiquetas.'''

from tkinter import *

root = Tk()     #Tk( ) es el objeto gráfico que representa a la ventana
                #raíz de la aplicación gráfica

def hola():
    print('Hola!!!!')

w = Label(root, text="Hello, world!")
x = Button(root, text="Hello", command = hola)
y = Label(root, text="Bye!!")
w.grid()
x.grid()
y.grid()



##w.grid(row=1, column=1)
##x.grid(row=1, column=2)
##y.grid(row=1, column=3)

##w.grid(row=1, column=1)
##x.grid(row=2, column=2)
##y.grid(row=3, column=3)


root.mainloop()

