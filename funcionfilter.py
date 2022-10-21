#la funcion filter siempre debe devolver True o False

numeros= [1,2,3,4,5,6,7,8,9,10]

def pares(x):
    if x % 2 == 0:
        return True
    return False

resultado = filter(pares, numeros)

print(list(resultado))