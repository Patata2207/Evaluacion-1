from django.urls import path
from . import views
urlpatterns = [
    path("", views.nuevo_registro, name="nuevo_registro"),
    path("registro/<int:id>/", views.motivo_registro, name="motivo_registro"),
    path("registro/nuevo/", views.nuevo_registro, name="nuevo_registro"),
    path("registro/editar/<int:id>/", views.editar_registro, name="editar_registro"),
    path("registro/eliminar/<int:id>/", views.eliminar_registro, name="eliminar_registro"),
    path("registro/registro_admim/", views.registro_admim, name="registro_admim"),
    path("registro/registro_visitas/", views.registro_visitas, name="registro_visitas"),
]