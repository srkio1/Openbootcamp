#Crea un script que le pida al usuario una lista de países (separados por comas).
#Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
#Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.


datos1=input("Introducir una lista de Paises:").upper()
datos2=list(datos1.split(","))
d3=list(set(datos2))
d4=sorted(d3)
print(d4)

#unicos=set(datos)







