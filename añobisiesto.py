
#para calcular si un año es bisiesto el residuo de dividir un numero entre 4 tiene que ser 0
def añobisiesto(num):
    if num % 4 == 0:
        print(f"El año {num} es bisiesto")
    else:
        print(f"El año {num} no es bisiesto")


añobisiesto(1988) 
    