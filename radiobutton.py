from tkinter import *

def seleccionar():
    
    label_seleccion.config(text=opcion.get())

def reset():
    opcion.set(None)
    label_seleccion.config(text="")

# Configuración de la raíz
window = Tk()

opcion = IntVar()

Radiobutton(window, text="Opción 1", variable=opcion, 
            value=1, command=seleccionar).pack()
Radiobutton(window, text="Opción 2", variable=opcion, 
            value=2, command=seleccionar).pack()
Radiobutton(window, text="Opción 3", variable=opcion,   
            value=3, command=seleccionar).pack()

label_seleccion = Label(window)
label_seleccion.pack()

Button(window, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la aplicación
window.mainloop()