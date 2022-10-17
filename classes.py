class Auto:
    _encendido= False
    
    def prender(self):
        self._encendido = True
        
    
    def apagar(self):
        self._encendido = False
    
    def isEncendido(self):
        if self._encendido == True:
            print("Donde nos vamos ?")
        elif self._encendido == False:
            print("Parece que hoy no saldremos")
        else:
            print("Parece que hay un error")
            
class Piezas(Auto):
    _npuertas = 0
    _nruedas = 0
    
    def puertas(self,_npuertas):
        return self._npuertas
    
h= Piezas()

h.prender()
print(h._npuertas)

   
