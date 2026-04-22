class Coche:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año
    def describir (self):
        return f"{self._marca} {self._modelo} {self._año}"
    
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

marca = str(input("Ingrese la marca de su coche"))
modelo = str (input("Ingrese el modelo de su coche"))
año= int (input("Ingrese el año de su coche"))

coche=Coche(marca, modelo, año)



print(coche.describir())