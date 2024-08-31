from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def index(request):
    return render(request, 'clientes/index.html')


def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
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
 
 