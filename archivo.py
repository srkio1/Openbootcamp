



    


#Abrir y guardar archivos
lista = [1,2,3,4,5,6,7,8,9,10,11,12]
archivo = open("archivo.txt", "a", encoding="utf-8") # r para solo lectura , w para escribir en el archivo y a para agregar datos en el archivo

for i in lista:
    a=str(lista.index(i))
    archivo.write(a +"\n")

archivo.close()

#Leer un archivo y mostrar linea por linea


archivo2 = open("archivo.txt", "r", encoding="utf-8")
for i in archivo2:
    print(i)
archivo2.close()



    