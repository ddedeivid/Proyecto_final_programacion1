class Vehiculo:
    def __init__(self, velocidad, combustible,aumento,freno):
        self.velocidad = velocidad
        self.combustible = combustible
        self.aumento = aumento
        self.freno = freno
    def acelerar(self):
        return f"El vehículo acelera usando combustible tipo {self.combustible} a una velocidad final de: {self.velocidad + self.aumento} km/h."
    def frenar(self):
        return f"El vehículo frena con una velocidad final de: {self.velocidad - self.freno} km/h."
    def detener(self):
        return f"El vehículo se detiene con una velocidad final de: 0 km/h."
class Carro(Vehiculo):
    def __init__(self, velocidad, combustible,aumento,freno, num_puertas):
        super().__init__(velocidad, combustible,aumento,freno)
        self.num_puertas = num_puertas

class Moto(Vehiculo):
    def __init__(self, velocidad, combustible,aumento,freno, tipo_moto):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_moto = tipo_moto
        
class Bicicleta(Vehiculo):
    def __init__(self, velocidad, combustible,aumento,freno, tipo_bici):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_bici = tipo_bici
        
class Avion(Vehiculo):
    def __init__(self, velocidad, combustible,aumento,freno, tipo_avion):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_avion = tipo_avion   
        
carro = Carro(100, "diesel", 20, 30, 4)
print(f"Carro: \nNúmero de puertas: {carro.num_puertas}")
print(carro.acelerar())
print(carro.frenar())
print(carro.detener())

moto = Moto(80, "gasolina", 15, 20, "deportiva")
print(f"\nMoto: \nTipo de moto: {moto.tipo_moto}")
print(moto.acelerar())
print(moto.frenar())
print(moto.detener())

bicicleta = Bicicleta(30, "fuerza humana", 10, 15, "montaña")
print(f"\nBicicleta: \nTipo de bicicleta: {bicicleta.tipo_bici}")
print(bicicleta.acelerar())
print(bicicleta.frenar())
print(bicicleta.detener())

avion = Avion(900, "queroseno", 200, 300, "militar")
print(f"\nAvión: \nTipo de avión: {avion.tipo_avion}")
print(avion.acelerar())     
print(avion.frenar())
print(avion.detener())