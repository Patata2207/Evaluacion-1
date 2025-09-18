from django import forms
from .models import Visita
import re
from django.core.exceptions import ValidationError

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ["nombre", "rut", "motivo", "hora_entrada", "hora_salida"]
        widgets = {
            "hora_entrada": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local", 
                    "class": "form-control"
                },
                format="%Y-%m-%dT%H:%M"
            ),
            "hora_salida": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local", 
                    "class": "form-control"
                },
                format="%Y-%m-%dT%H:%M"
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Para que muestre el valor en el formato correcto si ya existe
        self.fields["hora_entrada"].input_formats = ["%Y-%m-%dT%H:%M"]
        self.fields["hora_salida"].input_formats = ["%Y-%m-%dT%H:%M"]

    # Validar RUT con guion
    def clean_rut(self):
        rut = self.cleaned_data["rut"]
        if not re.match(r"^\d{7,8}-[0-9Kk]$", rut):
            raise ValidationError("El RUT debe tener el formato 12345678-9 o 12345678-K.")
        return rut
    # Validar formato de hora entrada
    def clean_hora_entrada(self):
        hora_entrada = self.cleaned_data["hora_entrada"]
        if not hora_entrada:
            raise ValidationError("La hora de entrada es obligatoria.")
        return hora_entrada

    # Validar formato de hora salida
    def clean_hora_salida(self):
        hora_salida = self.cleaned_data["hora_salida"]
        if not hora_salida:
            raise ValidationError("La hora de salida es obligatoria.")
        return hora_salida
