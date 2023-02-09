from django import forms

class CursoFormulario(forms.Form):
    curso=forms.CharField(max_length=20)
    camada=forms.IntegerField(max_value=999999, min_value=1)

class ProfesFormul(forms.Form):
    legajo=forms.IntegerField(max_value=9999, min_value=1)
    nombre_apellido=forms.CharField(max_length=60, min_length=5)
    email=forms.EmailField(max_length=30)
    curso_dictado=forms.CharField(max_length=30)
    
class EstudFormul(forms.Form):
    legajo=forms.IntegerField(max_value=999999, min_value=1)
    nombre_apellido=forms.CharField(max_length=60, min_length=5)
    email=forms.EmailField(max_length=30)
    cursando=forms.CharField(max_length=30)
    camada=forms.IntegerField(max_value=999999, min_value=1)