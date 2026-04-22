class Coche:
    """ Se define la clase Coche para que reciba los atributos marca, modelo y año."""
    def describir(self):
        """Método para imprimir la información del coche con atributos privados y métodos getter y setter"""
        return f"Marca: {self._marca}, \nModelo: {self._modelo}, \nAño: {self._año}"
        
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

# Primer coche
coche1 = Coche()                
coche1.set_marca("Toyota")         
coche1.set_modelo("Corolla")
coche1.set_año(2019)
print(f"Coche 1: \n{coche1.describir()}")

# Segundo coche
coche2 = Coche()               
coche2.set_marca("Honda")           
coche2.set_modelo("Civic")
coche2.set_año(2021)
print(f"\nCoche 2: \n{coche2.describir()}")

# Tercer coche
coche3 = Coche()               
coche3.set_marca("Ford")           
coche3.set_modelo("Mustang")
coche3.set_año(2020)
print(f"\nCoche 3: \n{coche3.describir()}")

# Cuarto coche
coche4 = Coche()               
coche4.set_marca("Chevrolet")       
coche4.set_modelo("Camaro")
coche4.set_año(2022)
print(f"\nCoche 4: \n{coche4.describir()}")

# Quinto coche
coche5 = Coche()               
coche5.set_marca("Tesla")           
coche5.set_modelo("Model 3")
coche5.set_año(2023)
print(f"\nCoche 5: \n{coche5.describir()}")