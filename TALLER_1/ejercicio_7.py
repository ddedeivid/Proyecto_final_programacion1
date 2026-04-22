from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "El perro hace: ¡Guau!"
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato hace: ¡Miau!"
class Serpiente(Animal):
    def hacer_sonido(self):
        return "La serpiente hace: ¡Sss!"
class Vaca(Animal):
    def hacer_sonido(self):
        return "La vaca hace: ¡Muu!"
    
# Lista de animales
animales = [Perro(), Gato(), Serpiente(), Vaca()]

# Recorrido de la lista de animales
print("\nSonidos de los animales:")
for animal in animales:
    print(animal.hacer_sonido())