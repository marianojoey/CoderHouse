from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("profesores/",profesor,name="Profesores"),
    path("estudiantes/",estudiante,name="Estudiantes"),
    path("cursos/",curso, name="Cursos"),
    path("buscar_camadas/",resultadosCamada,name="ResultadosBusqueda"),
    path("buscar_profes/",resultadosProfes,name="ResultadosProfesores"),
    path("buscar_alumnos/",resultadosEstudiantes,name="ResultadosEstudiantes"),
]
