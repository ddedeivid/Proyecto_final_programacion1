class Vehiculo:
    """Se crea la clase padre"""
    def __init__(self, velocidad, combustible,aumento,freno):
        """Se definen los atributos de la clase padre"""
        self.velocidad = velocidad
        self.combustible = combustible
        self.aumento = aumento
        self.freno = freno
    def acelerar(self):
        """Se define el método acelerar que devuelve un mensaje con la velocidad final al acelerar"""
        return f"El vehículo acelera usando combustible tipo {self.combustible} a una velocidad final de: {self.velocidad + self.aumento} km/h."
    def frenar(self):
        """Se define el método frenar que devuelve un mensaje con la velocidad final al frenar"""
        return f"El vehículo frena con una velocidad final de: {self.velocidad - self.freno} km/h."
    def detener(self):
        """Se define el método detener que devuelve un mensaje con la velocidad final al detenerse"""
        return f"El vehículo se detiene con una velocidad final de: 0 km/h."
    
class Carro(Vehiculo):
    """Se crea la clase hija Carro que hereda de Vehiculo"""
    def __init__(self, velocidad, combustible,aumento,freno, num_puertas):
        super().__init__(velocidad, combustible,aumento,freno)
        self.num_puertas = num_puertas
    def acelerar(self):
        """Se redefine el método acelerar para la clase Carro"""
        return "El carro acelera pisando el acelerador."

class Moto(Vehiculo):
    """Se crea la clase hija Moto que hereda de Vehiculo"""
    def __init__(self, velocidad, combustible,aumento,freno, tipo_moto):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_moto = tipo_moto
    def acelerar(self):
        """Se redefine el método acelerar para la clase Moto"""
        return "La moto acelera generando una rotación en la manija del acelerador."
        
class Bicicleta(Vehiculo):
    """Se crea la clase hija Bicicleta que hereda de Vehiculo"""
    def __init__(self, velocidad, combustible,aumento,freno, tipo_bici):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_bici = tipo_bici
    def acelerar(self):
        """Se redefine el método acelerar para la clase Bicicleta"""
        return "La bicicleta acelera pedaleando."
        
class Avion(Vehiculo):
    """Se crea la clase hija Avion que hereda de Vehiculo"""
    def __init__(self, velocidad, combustible,aumento,freno, tipo_avion):
        super().__init__(velocidad, combustible,aumento,freno)
        self.tipo_avion = tipo_avion 
    def acelerar(self):
        """Se redefine el método acelerar para la clase Avion"""
        return "El avión acelera generando empuje con los motores."  
        
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