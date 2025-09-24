
from django import forms
from .models import Visita
# Importa expresiones regulares para validación personalizada (valída usando patrones)
import re
# Importa la excepción de validación de Django
from django.core.exceptions import ValidationError


# Formulario basado en el modelo Visita
class VisitaForm(forms.ModelForm):
    class Meta:
        # Modelo asociado al formulario
        model = Visita
        # Campos que se mostrarán en el formulario
        fields = ["nombre", "rut", "motivo", "hora_entrada", "hora_salida"]
        # Widget bonito pa elegir la fecha y hora como calendario
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


    # Inicializamos el formulario y define los formatos de entrada para los campos de fecha y hora o(*￣▽￣*)ブ
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["hora_entrada"].input_formats = ["%Y-%m-%dT%H:%M"]
        self.fields["hora_salida"].input_formats = ["%Y-%m-%dT%H:%M"]



    # Validamos el campo RUT para asegurar el formato correcto ☆*: .｡. o(≧▽≦)o .｡.:*☆
    def clean_rut(self):
        rut = self.cleaned_data["rut"] 
        # El RUT debe tener 7 u 8 dígitos, un guion y un dígito verificador 
        if not re.match(r"^\d{7,8}-[0-9Kk]$", rut):
            raise ValidationError("El RUT debe tener el formato 12345678-9 o 12345678-K.")
        return rut


    # Validamos que la hora de entrada no esté vacía (❁´◡`❁)
    def clean_hora_entrada(self):
        hora_entrada = self.cleaned_data["hora_entrada"]
        if not hora_entrada:
            raise ValidationError("La hora de entrada es obligatoria.")
        return hora_entrada



    # Validamos que la hora de salida no esté vacía φ(*￣0￣)
    def clean_hora_salida(self):
        hora_salida = self.cleaned_data["hora_salida"]
        if not hora_salida:
            raise ValidationError("La hora de salida es obligatoria.")
        # También validamos que la hora de salida sea posterior a la hora de entrada
        hora_entrada = self.cleaned_data.get("hora_entrada")
        if hora_entrada and hora_salida <= hora_entrada:
            raise ValidationError("La hora de salida debe ser posterior a la hora de entrada.")
        return hora_salida
