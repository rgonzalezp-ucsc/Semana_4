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
# 2. Clase: Estudiante
class Estudiante(Persona):
    def __init__(self, rut, nombre, carrera, tiene_beca=False):
        super().__init__(rut, nombre)
        self.__carrera = carrera
        self.__calificaciones = []
        self.__tiene_beca = tiene_beca

    def registrar_nota(self, nota):
        if 1.0 <= nota <= 7.0:
            self.__calificaciones.append(nota)

    def calcular_promedio(self): 
        if not self.__calificaciones: return 0.0
        return sum(self.__calificaciones) / len(self.__calificaciones)

    def validar_aprobacion(self):
        return self.calcular_promedio() >= 4.0

    def validar_beca(self):
        return "Beca Activa" if self.__tiene_beca else "Sin Beneficios"

    def obtener_rol(self):
        return f"Estudiante de {self.__carrera}"
    
# 3. Clase: Docente
class Docente(Persona):
    def __init__(self, rut, nombre, especialidad):
        super().__init__(rut, nombre)
        self.__especialidad = especialidad
    def obtener_rol(self):
        return f"Docente de {self.__especialidad}"

