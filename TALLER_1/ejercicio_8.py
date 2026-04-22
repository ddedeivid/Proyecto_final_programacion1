from abc import ABC, abstractmethod
"""Se imoporta ABC y abstractmethod para crear una clase abstracta"""

class Volador(ABC):
    """Se crea la clase abstracta Volador"""
    @abstractmethod
    def volar(self):
        pass

class Pajaro(Volador):
    """Se crea la clase Pajaro que hereda de Volador"""
    def volar(self):
        return "El pájaro vuela batiendo sus alas."
class Avion(Volador):
    """Se crea la clase Avion que hereda de Volador"""
    def volar(self):
        return "El avión vuela generando empuje con sus motores."
    
# Lista de objetos voladores
voladores = [Pajaro(), Avion()]

# Recorrido de la lista de voladores
print("\nComportamiento de vuelo de los objetos:") 
for volador in voladores:
    print(volador.volar())