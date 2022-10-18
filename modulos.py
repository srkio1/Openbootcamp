#aqyu estamos importando el modulo de operaciones
import operaciones as op


opcion=1
opcion=2
opcion=3
opcion=4

print("""Calculadora basica 
      Opcion 1 Suma
      Opcion 2 Resta
      Opcion 3 Multiplicacion
      Opcion 4 dividir
      opcion 5 salir""")
int(input("elija un numero de la lista: "))


if opcion == 1:
    print(op.suma(5,5))
elif opcion == 2:
    print(op.resta(4,4))
elif opcion == 3:
    print(op.multiplicar(4,4))
elif opcion== 4:
    print(op.dividir(6,2))
elif opcion==5:
    print("Hasta luego")
else:
    print("algo salio mal")
    


