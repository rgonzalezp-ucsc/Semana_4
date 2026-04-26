Evaluación Semana 4
____________________________
* Alumno: Rodrigo I. González P.
* Asignatura: Desarrollo de Sistemas Orientado a Objetos
* Profesor: Pablo Lastra
__________________________________________

** Creación de sistema académico **
__________________________________
Este proyecto es una solución de software orientada a objetos diseñada para automatizar procesos básicos de una universidad.
* El sistema permite gestionar la información de estudiantes, docentes y asignaturas, al facilitar tareas esenciales como la inscripción de cursos, el registro de calificaciones y la validación automática de aprobación o reprobación de los alumnos.
* El diseño se centra en la modularidad y reutilización de código, gracias a la aplicacion los pilares fundamentales de la POO: abstracción, encapsulamiento, herencia y polimorfismo.

Instrucciones de Ejecución
___________________________
 Se requiere tener instalado lenguaje Python en el equipo previo a la puesta en marcha del sistema, luego seguir los siguientes pasos:

* Descarga los archivos "evaluac_04.py" que es el código en Python y "Diagram_04.puml" (diagrama UML), ambos ubicados en el repositorio "Semana_4".
* Abre una terminal o consola de comandos (Recomendado: Visual Studio Code).
* Navega hasta la carpeta del proyecto.
* Ejecuta el PlantUML (.puml) para visualizar Diagrama del software.
* Ejecuta el programa (.py) en "Run Python File" en VSC).
* El sistema mostrará los reportes y resultados directamente en la terminal de salida.

Estructura del Proyecto
___________________________
El código está organizado de la siguiente manera:

* Clase Base (Persona): Contiene los datos comunes (RUT, nombre) para evitar duplicar código.
* Clases Derivadas (Estudiante y Docente): Especializaciones que heredan de Persona y añaden lógica propia, como el cálculo de promedios o especialidades.
* Orquestación (SistemaAcademico): Existe una clase coordinadora que gestiona el flujo de los datos sin concentrar toda la lógica en un solo lugar, lo que asegura un bajo acoplamiento.
* Encapsulamiento: Todos los datos sensibles están protegidos (atributos privados), accediendo a ellos solo mediante métodos autorizados.
* Diagrama de Clases UML desarrollado en PlantUML, representa la arquitectura técnica del sistema.

Tecnologías Utilizadas
________________________
* Visual Studio Code para terminal de código o consola de comandos.
* Lenguaje: Python
* Modelamiento: PlantUML para el diseño de diagrama.
* Gestión de Datos: Librería datetime para el manejo profesional de fechas.
* Control de Versiones: Se instala Git y se sincroniza en VSC, se crea cuenta en GitHub.com para creacion de Cummits y acceder al historial de cambios.
