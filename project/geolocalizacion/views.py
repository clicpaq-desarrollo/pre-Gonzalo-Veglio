from django.shortcuts import render, redirect
from .models import Provincia, Localidad
from .forms import ProvinciaForm, LocalidadForm
from django.db.models import Q

 
 
def provincia_list(request): 
    provincias = Provincia.objects.all()
    context = {"object_list": provincias}
    return render(request, "geolocalizacion/provincia_list.html", context)
 
 
def provincia_create(request):
    if request.method == 'POST':
        form = ProvinciaForm(request.POST)
    if request.method == 'GET':
        form = ProvinciaForm()
    if form.is_valid():
        form.save()
        return redirect ('geolocalizacion:provincia_list')
    return render(request, 'geolocalizacion/provincia_create.html', {'form': form})
 

def provincia_update(request, pk: int):
    query = Provincia.objects.get(id=pk)
    if request.method == 'GET':
        form = ProvinciaForm(instance=query)

    if request.method == 'POST':
        form = ProvinciaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('geolocalizacion:provincia_list')
    return render(request, 'geolocalizacion/provincia_create.html', {'form': form})
 
def provincia_delete(request, pk: int):
    query = Provincia.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('provincias:provincia_list')
    return render(request, 'geolocalizacion/provincia_confirm_delete.html', {'object': query})

 
def localidad_list(request): 
    localidades = Localidad.objects.all()
    context = {"object_list": localidades}
    return render(request, "geolocalizacion/localidad_list.html", context)
 
 
def localidad_create(request):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
    if request.method == 'GET':
        form = LocalidadForm()
    if form.is_valid():
        form.save()
        return redirect ('geolocalizacion:localidad_list')
    return render(request, 'geolocalizacion/localidad_create.html', {'form': form})
 

def localidad_update(request, pk: int):
    query = Localidad.objects.get(id=pk)
    if request.method == 'GET':
        form = LocalidadForm(instance=query)

    if request.method == 'POST':
        form = LocalidadForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('geolocalizacion:localidad_list')
    return render(request, 'geolocalizacion/localidad_create.html', {'form': form})
 
def localidad_delete(request, pk: int):
    query = Localidad.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('geolocalizacion:localidad_list')
    return render(request, 'geolocalizacion/localidad_confirm_delete.html', {'object': query})




