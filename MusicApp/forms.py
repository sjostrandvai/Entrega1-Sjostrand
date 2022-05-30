import email
from django import forms


class MusicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=40)


class TemaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    duracion = forms.FloatField()
    añoLanzamiento = forms.IntegerField()
    autor = forms.CharField(max_length=40)


class BandaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
