from ctypes import resize
import tkinter



windows = tkinter.Tk()

label_principal = tkinter.Label(text="Soy el Label principal")
label_principal.pack(expand=True)
input_principal = tkinter.Listbox(listvariable="Agua"+"Azucar")
input_principal.pack(expand=True)
windows.mainloop()