from django.shortcuts import render, redirect
from .models import Mecanico
from .forms import MecanicoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def inicio(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'paginas/index.html', {'mecanicos': mecanicos})

def mecanico(request):
    mecanicos = Mecanico.objects.all()
    return render(request, 'paginas/index.html', {'mecanicos': mecanicos})

@login_required
def crearmec(request):
    formulario = MecanicoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'mecanicos/crearcard.html', {'formulario':formulario})

def editarmec(request, id):
    mecanico = Mecanico.objects.get(id=id)
    formulario = MecanicoForm(request.POST or None, request.FILES or None, instance=mecanico)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('inicio')
    return render(request, 'mecanicos/crearcard.html', {'formulario':formulario})

def eliminarmec(request, id):
    mecanico = Mecanico.objects.get(id=id)
    mecanico.delete()
    return redirect('inicio')



