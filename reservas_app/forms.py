from django import forms
from .models import Restaurante, Reserva

class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_comida', 'direccion']

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['restaurante', 'dia', 'hora', 'personas']  # Añadir personas aquí

    dia = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    personas = forms.IntegerField(min_value=1)