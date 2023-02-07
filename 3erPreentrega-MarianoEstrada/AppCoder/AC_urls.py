from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    path("profesores/",profesor,name="Profesores"),
    path("estudiantes/",estudiante,name="Estudiantes"),
    path("cursos/",curso, name="Cursos"),
    path("curso_formulario/",cursoFormulario,name="FormularioCurso"),
    path("profes_formulario/",profesFormul,name="FormularioProfesores"),
    path("estud_formulario/",alumnFormul,name="FormularioAlumnos"),
    path("busqueda_camada/",busquedaCamada,name="BuscarCamada"),
    path("camadas/",resultadosCamada,name="ResultadosBusqueda"),
    path("apellido_profes/",resultadosProfes,name="ResultadosProfesores"),
    path("apellido_alumnos/",resultadosEstudiantes,name="ResultadosEstudiantes"),
]
