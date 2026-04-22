class Coche:
    """ Clase Coche con atributos marca, modelo y año."""    
    def __init__(self, new_marca, new_modelo, new_año):
        """Aquí se define el constructor de la clase Coche, que recibe los parámetros marca, modelo y año."""
        self.set_marca(new_marca)
        self.set_modelo(new_modelo)
        self.set_año(new_año)
        
    def describir(self):
        """Aquí se usan los datos guardados en el constructor para describir el coche, retornando una cadena con la marca, modelo y año del coche."""
        return f"Marca: {self._marca}, \nModelo: {self._modelo}, \nAño: {self._año}"
    
    #getters y setters para cada atributo, con validación de datos
    def get_marca(self):
        return self._marca
    
    def set_marca(self, new_marca):
        if new_marca != "":
            self._marca = new_marca
        else:
            print("La marca no puede estar vacía.") 
    
    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, new_modelo):
        if new_modelo != "":
            self._modelo = new_modelo
        else:
            print("El modelo no puede estar vacío.")   
            
    def get_año(self):
        return self._año
            
    def set_año(self, new_año):
        if new_año > 0:
            self._año = new_año
        else:
            print("El año debe ser un valor positivo.")    
    

# Primer coche
coche1 = Coche("Toyota", "Corolla", 2019)
print(f"Coche 1: \n{coche1.describir()}")

# Segundo coche
coche2 = Coche("Honda", "Civic", 2021)
print('\n'f"Coche 2: \n{coche2.describir()}")

# Tercer coche
coche3 = Coche("Ford", "Mustang", 2020)
print('\n'f"Coche 3: \n{coche3.describir()}")

# Cuarto coche
coche4 = Coche("Chevrolet", "Camaro", 2022)
print('\n'f"Coche 4: \n{coche4.describir()}")

# Quinto coche
coche5 = Coche("Tesla", "Model 3", 2023)
print('\n'f"Coche 5: \n{coche5.describir()}")

# Sexto coche
coche6 = Coche("BMW", "X5", 2026)
print('\n'f"Coche 6: \n{coche6.describir()}")