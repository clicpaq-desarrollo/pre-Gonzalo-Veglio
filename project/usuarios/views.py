from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def index(request):
    return render(request, 'usuarios/index.html')


def usuario_list(request):
    query = Usuario.objects.all()
    context = {"object_list": query}
    return render(request, "usuarios/usuario_list.html", context)

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
    if request.method == 'GET':
        form = UsuarioForm()
    if form.is_valid():
        form.save()
        return redirect ('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_create.html', {'form': form})
 
 