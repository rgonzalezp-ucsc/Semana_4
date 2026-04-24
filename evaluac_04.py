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
    
# 4. Clase: Asignatura
class Asignatura:
    def __init__(self, codigo, nombre):
        self.__codigo = codigo
        self.__nombre = nombre

    def get_info(self):
        return f"[{self.__codigo}] {self.__nombre}"

# 5. Clase: Sección (Sistema)
class Seccion:
    def __init__(self, id_seccion, asignatura, docente):
        self.__id_seccion = id_seccion
        self.__asignatura = asignatura
        self.__docente = docente
        self.__estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.__estudiantes.append(estudiante)

    def generar_reporte_seccion(self): 
        print(f"\n--- REPORTE: {self.__asignatura.get_info()} ---")
        print(f"Docente a cargo: {self.__docente.get_nombre()}")
        print(f"ID Sección: {self.__id_seccion}")
        print("-" * 30)
        for e in self.__estudiantes:
            estado = "APROBADO" if e.validar_aprobacion() else "REPROBADO"
            print(f"Alumno: {e.get_nombre()} | Promedio: {e.calcular_promedio():.1f} | {estado}")
            print(f"Estado Financiero: {e.validar_beca()}")



