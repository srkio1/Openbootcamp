from select import select


class Vehiculo:
    _color= "color"
    _ruedas = 0
    _puertas = 0

    def color(self):
        self._color = "Azul"
    def ruedas(self):
        self._ruedas=4
    
    def puertas(self):
        self._puertas=5


class Coche(Vehiculo):
    _velocidad = 100
    _cilindradas = 200
    
    def velocidades(self):
        self._velocidad = 100
    def cilindrada(self):
        self._cilindradas = 200


coche = Coche()

coche.color()
coche.ruedas()
coche.puertas()
coche.velocidades()
coche.cilindrada()

print(f"Color: {coche._color}\nRuedas: {coche._ruedas}\nPuertas: {coche._puertas}\nVelocidad: {coche._velocidad}\nCilindradas: {coche._cilindradas}")

