class Alumno:
    _nombre = ""
    _nota = 0
    _aprobado= ""
    
    def nombre(self):
         return self._nombre
    def nota(self):
        return self._nota
    
    def aprobado(self):
        if self._nota> 51:
            self._aprobado="Aprobado"
        else:
            self._aprobado="Reprobado"
            


a1= Alumno()

a1._nombre = input("Inserte el nombre del alumno: ")
a1._nota = int(input("ingrese la nota del Alumno: "))
a1.aprobado()
print(f"Alumno: {a1._nombre}\nNota: {a1._nota}\n{a1._aprobado}")