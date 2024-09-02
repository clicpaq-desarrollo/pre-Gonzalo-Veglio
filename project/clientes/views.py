from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.db.models import Q

def index(request):
    return render(request, 'clientes/index.html')
 
def cliente_list(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter( razon_social__icontains=query )
    else:
        clientes = Cliente.objects.all()
    context = {"object_list": clientes}
    return render(request, "clientes/cliente_list.html", context)
 
 
def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
    if request.method == 'GET':
        form = ClienteForm()
    if form.is_valid():
        form.save()
        return redirect ('clientes:cliente_list')
    return render(request, 'clientes/cliente_create.html', {'form': form})
 

def cliente_update(request, pk: int):
    query = Cliente.objects.get(id=pk)
    if request.method == 'GET':
        form = ClienteForm(instance=query)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('clientes:cliente_list')
    return render(request, 'clientes/cliente_create.html', {'form': form})
 
def cliente_delete(request, pk: int):
    query = Cliente.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('clientes:cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'object': query})
    