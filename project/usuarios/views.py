from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm
from django.db.models import Q

def index(request):
    return render(request, 'usuarios/index.html')


 

def usuario_list(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query)
        )
    else:
        usuarios = Usuario.objects.all()
    context = {"object_list": usuarios}
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

def usuario_delete(request, pk: int):
    query = Usuario.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('usuarios:usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'object': query})
 
 