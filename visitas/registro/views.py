from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm

# Lista de visitas
def registro_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'visitas/registro_visitas.html', {'visitas': visitas})

# Ver detalle de una visita (motivo, etc.)
def motivo_registro(request, id):
    visita = get_object_or_404(Visita, id=id)
    return render(request, 'visitas/motivo_registro.html', {'visita': visita})


def nuevo_registro(request):
    mensaje = None
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "¡Visita agendada correctamente!"
            form = VisitaForm()  # Limpiar el formulario
    else:
        form = VisitaForm()
    return render(request, "visitas/nuevo_registro.html", {"form": form, "mensaje": mensaje})

# Editar visita
def editar_registro(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('registro_visitas')
        else:
            print(form.errors)  # 👈 Debug para ver errores
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'visitas/editar_registro.html', {'form': form})


# Eliminar visita
def eliminar_registro(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('registro_visitas')
    return render(request, 'visitas/eliminar_registro.html', {'visita': visita})


def registro_admim(request):
    error = None
    if request.method == "POST":
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        if correo == "admin@admin.com" and password == "1234":
            return redirect("registro_visitas")
        else:
            error = "Correo o contraseña incorrectos."
    return render(request, 'visitas/registro_admim.html', {"error": error})
