class Coche:
    def describir(self):
        return f"{self.marca} {self.modelo} {self.año}"


marca = input("Ingrese la marca de su coche: ")
modelo = input("Ingrese el modelo de su coche: ")
año = int(input("Ingrese el año de su coche: "))

coche = Coche()  # objeto vacío

coche.marca = marca
coche.modelo = modelo
coche.año = año

print(coche.describir())