class Coche:
    def describir(self):
        return f"{self.marca} {self.modelo} {self.año}"
        
       #getters
    def get_marca(self):
        return self._marca
    def get_modelo(self):
        return self._modelo
    def get_año(self):
        return self._año
    #setters
    def set_marca(self, marca):
        self._marca = marca
    def set_modelo(self, modelo):
        self._modelo = modelo
    def set_año(self, año):
        self._año = año


marca = input("Ingrese la marca de su coche: ")
modelo = input("Ingrese el modelo de su coche: ")
año = int(input("Ingrese el año de su coche: "))

coche = Coche()  

coche.marca = marca
coche.modelo = modelo
coche.año = año

print(coche.describir())