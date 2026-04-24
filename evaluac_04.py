from abc import ABC, abstractmethod
from datetime import datetime

# 1. Clase Base
class Persona(ABC):
    def __init__(self, rut, nombre):
        self.__rut = rut  # Encapsulamiento
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    @abstractmethod
    def obtener_rol(self): # Polimorfismo
        pass
