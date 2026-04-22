from abc import ABC, abstractmethod
"""Se imoporta ABC y abstractmethod para crear una clase abstracta"""

class Animal(ABC):
    """Se crea la clase abstracta Animal"""
    @abstractmethod
    def hacer_sonido(self):
        pass
class Perro(Animal):
    """Se crea la clase Perro que hereda de Animal"""
    def hacer_sonido(self):
        return "El perro hace: ¡Guau!"
class Gato(Animal):
    """Se crea la clase Gato que hereda de Animal"""
    def hacer_sonido(self):
        return "El gato hace: ¡Miau!"
class Serpiente(Animal):
    """Se crea la clase Serpiente que hereda de Animal"""
    def hacer_sonido(self):
        return "La serpiente hace: ¡Sss!"
class Vaca(Animal):
    """Se crea la clase Vaca que hereda de Animal"""
    def hacer_sonido(self):
        return "La vaca hace: ¡Muu!"
    
# Lista de animales
animales = [Perro(), Gato(), Serpiente(), Vaca()]

# Recorrido de la lista de animales
print("\nSonidos de los animales:")
for animal in animales:
    print(animal.hacer_sonido())