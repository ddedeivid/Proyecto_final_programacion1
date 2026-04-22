class Motor:
    """ Se define la clase Motor con atributos potencia y tipo."""
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

class Coche:
    """ Se define la clase Coche para que reciba los atributos marca, modelo y motor."""
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

# Creación de objetos Motor y Coche 1        
motor1 = Motor(150, "gasolina")       # objeto Motor
coche1 = Coche("Toyota", "Corolla", motor1)  # se lo pasas al Coche

print(f"\nCaracterísticas del coche 1:\nMarca: {coche1.marca}") 
print(f"Modelo del coche: {coche1.modelo}")
print(f"Potencia del motor: {coche1.motor.potencia}")
print(f"Tipo: {coche1.motor.tipo}")

# Creación de objetos Motor y Coche 2
motor2 = Motor(200, "diésel")         # otro objeto Motor
coche2 = Coche("Honda", "Civic", motor2)  # se

print(f"\nCaracterísticas del coche 2:\nMarca: {coche2.marca}") 
print(f"Modelo del coche: {coche2.modelo}") 
print(f"Potencia del motor: {coche2.motor.potencia}")
print(f"Tipo: {coche2.motor.tipo}")