from django.shortcuts import render, get_object_or_404, redirect
from .models import Visita
from .forms import VisitaForm

# Create your views here.
def lista_visitas(request):
    visitas = Visita.objects.all()
    return render(request, 'Sistema/lista_visitas.html', {'visitas': visitas})

def detalle_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    return render(request, 'Sistema/detalle_visita.html', {'visita': visita})

def nueva_visita(request):
    if request.method == 'POST':
        form = VisitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm()
    return render(request, 'Sistema/nueva_visita.html', {'form': form})

def editar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            form.save()
            return redirect('lista_visitas')
    else:
        form = VisitaForm(instance=visita)
    return render(request, 'Sistema/editar_producto.html', {'form': form})

def eliminar_visita(request, id):
    visita = get_object_or_404(Visita, id=id)
    if request.method == 'POST':
        visita.delete()
        return redirect('lista_visitas')
    return render(request, 'Sistema/eliminar_visita.html', {'visita': visita})