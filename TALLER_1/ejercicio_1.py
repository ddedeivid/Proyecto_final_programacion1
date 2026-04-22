## Clase Coche con atributos marca, modelo y año.
class Coche:
    
    ## Aquí se define el constructor de la clase Coche, que recibe los parámetros marca, modelo y año.
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    ## Aquí se usan los datos guardados en el constructor para describir el coche, retornando una cadena con la marca, modelo y año del coche.    
    def describir(self):
        return f"{self.marca} {self.modelo} {self.año}"

## Primer coche
coche1 = Coche("Toyota", "Corolla", 2019)
print(f"Marca: {coche1.marca}")
print(f"Modelo: {coche1.modelo}")
print(f"Año: {coche1.año}")

## Segundo coche
coche2 = Coche("Honda", "Civic", 2021)
print('\n'f"Marca: {coche2.marca}")
print(f"Modelo: {coche2.modelo}")
print(f"Año: {coche2.año}")

## Tercer coche
coche3 = Coche("Ford", "Mustang", 2020)
print('\n'f"Marca: {coche3.marca}")
print(f"Modelo: {coche3.modelo}")
print(f"Año: {coche3.año}")

## Cuarto coche
coche4 = Coche("Chevrolet", "Camaro", 2022)
print('\n'f"Marca: {coche4.marca}")
print(f"Modelo: {coche4.modelo}")
print(f"Año: {coche4.año}")

## Quinto coche
coche5 = Coche("Tesla", "Model 3", 2023)
print('\n'f"Marca: {coche5.marca}")
print(f"Modelo: {coche5.modelo}")
print(f"Año: {coche5.año}")