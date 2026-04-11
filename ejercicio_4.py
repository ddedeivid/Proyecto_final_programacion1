class vehiculo:
    def __init__(self, velocidad, combustible,aumento,freno):
        self.velocidad = velocidad
        self.combustible = combustible
        self.aumento = aumento
        self.freno = freno
    def acelerar(self):
        return f"La velocidad final del vehiculo que usa {self.combustible} es de {self.velocidad+self.aumento} km/h"
    def frenar(self):
        return f"La velocidad final es de {self.velocidad-self.freno} km/h"
    def detener(self):
        return f"La velocidad final es de 0 km/h"




velocidad = 80
aumento = 20
freno = 10
combustible = "ACPM"