peso = float(input("Introduce tu peso en Kg: "))
altura = float(input("Altura en metros: "))

r = peso / (altura**2)
imc = round(r ,2)

print(f"Tu indice de masa corporal es {imc}")