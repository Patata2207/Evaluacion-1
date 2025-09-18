from django import forms
from .models import Visita
import re
from django.core.exceptions import ValidationError

class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = ["nombre", "rut", "motivo", "hora_entrada", "hora_salida"]
        widgets = {
            "hora_entrada": forms.TextInput(attrs={
                "placeholder": "2025-09-16 09:30:00"
            }),
            "hora_salida": forms.TextInput(attrs={
                "placeholder": "2025-09-16 18:00:00"
            }),
        }

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
