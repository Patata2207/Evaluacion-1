import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Visita
from .forms import VisitaForm


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    form = VisitaForm


    list_display  = ("nombre", "rut", "motivo", "hora_entrada", "hora_salida")
    search_fields = ("rut", "nombre")
    list_filter   = ("hora_entrada",)
    ordering      = ("-hora_entrada",)

    actions = ["export_as_csv"]

    @admin.action(description="Exportar seleccionados a CSV")
    def export_as_csv(self, request, queryset):
        """
        Genera un archivo CSV con los registros seleccionados.
        """
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f'attachment; filename={meta.model_name}.csv'
        )

        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            writer.writerow([getattr(obj, f) for f in field_names])

        return response