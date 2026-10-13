#Clase abstracta Figura con area() y perimetro(); implementa Circulo, Rectangulo y Cuadrado.

from abc import ABC, abstractmethod
from math import pi
 
class Figura(ABC):
 
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimetro(self): ...
 
class Circulo(Figura):
    def __init__(self, radio):
        self._radio = radio

    def area(self):
        return pi * (self._radio ** 2)
 
    def perimetro(self):
        return pi * self._radio * 2
    
class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    def perimetro(self):
        return  (2*self._largo) + (2*self._ancho)
    def area(self):
        return self._ancho * self._largo

class Cuadrado(Figura):
    def __init__(self, lado):
        self._lado = lado

    def perimetro(self):
        return self._lado * 4
    
    def area(self):
        return self._lado ** 2

circ = Circulo(2)
print(round(circ.area(),2))
print(round(circ.perimetro(),2))

rect = Rectangulo(6,2)
print(rect.area())
print(rect.perimetro())

cua = Cuadrado(6)
print(cua.area())
print(cua.perimetro())

