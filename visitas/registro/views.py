# Importa funciones útiles de Django para renderizar plantillas, obtener objetos o devolver redirecciones
from django.shortcuts import render, get_object_or_404, redirect
# Importa el modelo Visita y el formulario asociado
from .models import Visita
from .forms import VisitaForm

# Vista que muestra la lista de todas las visitas registradas
def registro_visitas(request):
    # Obtiene todas las visitas de la base de datos
    visitas = Visita.objects.all()
    # Carga la lista de visitas
    return render(request, 'visitas/registro_visitas.html', {'visitas': visitas})

# Vista para ver el detalle de una visita específica, usando su id O.O
def motivo_registro(request, id):
    # Busca la visita por id, si no existe muestra error 404
    visita = get_object_or_404(Visita, id=id)
    # Carga los datos de la visita
    return render(request, 'visitas/motivo_registro.html', {'visita': visita})


# Vista para crear un nuevo registro de visita (*/ω＼*)
def nuevo_registro(request):
    mensaje = None 
    if request.method == "POST":
        # Crea el formulario con los datos enviados por el usuario
        form = VisitaForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda la visita
            form.save()
            mensaje = "¡Visita agendada correctamente!"
            form = VisitaForm()  # Limpia el formulario para permitir otro registro
    else:
        # Si es GET, muestra el formulario vacío
        form = VisitaForm()
    # Crea el formulario y el mensaje
    return render(request, "visitas/nuevo_registro.html", {"form": form, "mensaje": mensaje})

# Vista para editar una visita existente ψ(｀∇´)ψ
def editar_registro(request, id):
    # Busca la visita por id
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        # Formulario con datos nuevos y la instancia a editar
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            # Guarda los cambios
            form.save()
            return redirect('registro_visitas')  # Redirige a la lista de visitas
        else:
            print(form.errors)  # Muestra errores en consola para depuración
    else:
        # Formulario con los datos actuales
        form = VisitaForm(instance=visita)
    # Renderiza la plantilla de edición
    return render(request, 'visitas/editar_registro.html', {'form': form})


# Vista para eliminar una visita existente (oﾟvﾟ)ノ
def eliminar_registro(request, id):
    # Busca la visita por id
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('registro_visitas')  # Redirige a la lista de visitas
    # Renderiza la plantilla de confirmación de eliminación
    return render(request, 'visitas/eliminar_registro.html', {'visita': visita})


# Vista para el login de administrador (￣y▽￣)╭ Ohohoho.....
def registro_admim(request):
    error = None  
    if request.method == "POST":
        # Obtiene el correo y la contraseña del formulario
        correo = request.POST.get("correo")
        contrasena = request.POST.get("contrasena")
        # Credenciales fijas para el acceso de administrador
        if correo == "patata@gmail.com" and contrasena == "123456":
            return redirect("registro_visitas")  
        else:
            error = "Correo o contraseña incorrectos."
    # Renderiza el formulario de login de administrador, mostrando un mensaje de error si corresponde
    return render(request, 'visitas/registro_admim.html', {"error": error})
