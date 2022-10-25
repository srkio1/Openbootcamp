from pprint import pprint
import tkinter as tk




# Configuración de la raíz
window = tk.Tk()
window.title("Lista de Elementos")


lista=["Elemento1", "Elemento2", "Elemento3", "Elemento4"]
lista_item=tk.StringVar(value=lista)
listbox =tk.Listbox(window, listvariable=lista_item).pack()

label = tk.Label(window , text="Hola").pack()




#label_seleccion.pack()

#Button(window, text="Reiniciar", command=reset).pack()

# Finalmente bucle de la aplicación
window.mainloop()