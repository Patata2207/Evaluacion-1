from django.contrib import admin
from .models import Visita
import csv
from django.http import HttpResponse

@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    list_display = ('nombre','rut', 'motivo', 'hora_entrada', 'hora_salida' )
    search_fields = ('rut','nombre')
    list_filter = ('hora_entrada',)
    ordering = ('-hora_entrada',)
    actions = ['export_as_csv']


    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

@admin.action(description='Exportar como CSV')
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response