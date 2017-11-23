'''Crear una ventana que contenga tres etiquetas.'''

from tkinter import *

root = Tk()     #Tk( ) es el objeto gráfico que representa a la ventana
                #raíz de la aplicación gráfica

w = Label(root, text="Hello, world!")
x = Label(root, text="How are you?")
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

w = tk.Button(parent, option=value, ...)
