
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


#Ingresamos validadores en este archivo por que aqui es donde sew define como se reciben y procesan datos que se ingresan

    # Inicializamos el formulario y define los formatos de entrada para los campos de fecha y hora o(*￣▽￣*)ブ
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    # Validamos el campo RUT para asegurar el formato correcto ☆*: .｡. o(≧▽≦)o .｡.:*☆
    def clean_rut(self):
        rut = self.cleaned_data["rut"] 
        # El RUT debe tener 7 u 8 dígitos, un guion y un dígito verificador 
        if not re.match(r"^\d{7,8}-[0-9Kk]$", rut):
            raise ValidationError("El RUT debe tener el formato 12345678-9 o 12345678-K.")
        return rut