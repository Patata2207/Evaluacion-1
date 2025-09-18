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
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro_visitas")
    else:
        form = VisitaForm()
    return render(request, "visitas/nuevo_registro.html", {"form": form})

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
