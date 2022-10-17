class Alumno:
    _nombre = ""
    _nota = 0
    _aprobado= ""
    
    def nombre(self):
        self._nombre = "Roberto"
    def nota(self):
        self._nota = 60
    
    def aprobado(self):
        if self._nota> 51:
            self._aprobado="Aprobado"
        else:
            self._aprobado="Reprobado"
            


a1= Alumno()

a1.nombre()
a1.nota()
a1.aprobado()
print(f"Alumno: {a1._nombre}\nNota: {a1._nota}\n{a1._aprobado}")