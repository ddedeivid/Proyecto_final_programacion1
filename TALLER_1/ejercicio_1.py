class Coche:
    """ Se define la clase Coche para que reciba los atributos marca, modelo y año."""
    def describir(self):
        """Método para imprimir la información del coche"""
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.año}"

# Primer coche
coche1 = Coche()                
coche1.marca = "Toyota"         
coche1.modelo = "Corolla"
coche1.año = 2019
print(f"Coche 1: \n{coche1.describir()}")

# Segundo coche
coche2 = Coche()               
coche2.marca = "Honda"           
coche2.modelo = "Civic"
coche2.año = 2021
print(f"\nCoche 2: \n{coche2.describir()}")

# Tercer coche
coche3 = Coche()               
coche3.marca = "Ford"           
coche3.modelo = "Mustang"
coche3.año = 2020
print(f"\nCoche 3: \n{coche3.describir()}")

# Cuarto coche
coche4 = Coche()               
coche4.marca = "Chevrolet"       
coche4.modelo = "Camaro"
coche4.año = 2022
print(f"\nCoche 4: \n{coche4.describir()}")

# Quinto coche
coche5 = Coche()               
coche5.marca = "Tesla"           
coche5.modelo = "Model 3"
coche5.año = 2023
print(f"\nCoche 5: \n{coche5.describir()}")