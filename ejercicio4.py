

#ejercicio para mostrar numeros del 1 al 100 en orden descendente
num= 0
lista=[]

for num in range(100):
    num += 1
    lista.append(num)
    
lista.reverse()
print(lista)
