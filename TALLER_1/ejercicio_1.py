## Clase Coche con atributos marca, modelo y año.
class Coche:
    
    ## Aquí se define el constructor de la clase Coche, que recibe los parámetros marca, modelo y año.
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    ## Aquí se usan los datos guardados en el constructor para describir el coche, retornando una cadena con la marca, modelo y año del coche.    
    def describir(self):
        return f"Marca: {self.marca}, \nModelo: {self.modelo}, \nAño: {self.año}"

## Primer coche
coche1 = Coche("Toyota", "Corolla", 2019)
print(f"Coche 1: \n{coche1.describir()}")

## Segundo coche
coche2 = Coche("Honda", "Civic", 2021)
print('\n'f"Coche 2: \n{coche2.describir()}")

## Tercer coche
coche3 = Coche("Ford", "Mustang", 2020)
print('\n'f"Coche 3: \n{coche3.describir()}")

## Cuarto coche
coche4 = Coche("Chevrolet", "Camaro", 2022)
print('\n'f"Coche 4: \n{coche4.describir()}")

## Quinto coche
coche5 = Coche("Tesla", "Model 3", 2023)
print('\n'f"Coche 5: \n{coche5.describir()}")