from ..models import *
from django.forms import ModelForm, Form, DateInput
from django import forms


class DiscograficaForm(ModelForm):
    class Meta:
        model = Discografica
        fields = ['nombre', 'pais']


class ArtistaForm(ModelForm):
    class Meta:
        model = Artista
        fields = ['nombre', 'pais','discografica','fecha','estilos']
        widgets = {'fecha':DateInput(attrs={'type':'date'})}


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'password','email','nombre','apellidos']
        widgets = {
            'password': forms.PasswordInput(),
        }


class TiempoForm(ModelForm):
    class Meta:
        model = Tiempo
        fields = ['tiempo', 'usuario', 'artista']


class Buscador(Form):
    usuario = forms.CharField(label='Usuario', max_length=100)