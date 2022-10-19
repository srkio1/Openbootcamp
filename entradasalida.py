#Guardando una clase en un archivo

class Vehiculo:
    color= ""
    ruedas = 0
    puertas = 0
    marca = ""

    def color(self):
        return self.color
    def ruedas(self):
        return self.ruedas
    
    def puertas(self):
        return self.puertas
    def marca(self):
        return self.marca
v1 = Vehiculo()


v1.color = "Azul"
v1.ruedas= 4
v1.puertas=4
v1.marca= "Toyota"

dic={"auto":v1.color,"Ruedas": v1.ruedas, "Puertas": v1.puertas,"Marca": v1.marca}
archivo2 = open("archivo2.txt", "a", encoding="utf-8")
a=str(dic)
archivo2.write(a+"\n")
archivo2.close()