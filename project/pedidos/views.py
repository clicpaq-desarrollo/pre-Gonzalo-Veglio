from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm
from django.db.models import Q
from django.contrib import messages 

def index(request):
    return render(request, 'pedidos/index.html')

 
def pedido_list(request):
    query = request.GET.get('q')
    if query:
        pedidos = Pedido.objects.filter(
            Q(nombre_destinatario__icontains=query) | 
            Q(apellido_destinatario__icontains=query)
        )
    else:
        pedidos = Pedido.objects.all()
    context = {"object_list": pedidos}
    return render(request, "pedidos/pedido_list.html", context)
 
def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
    if request.method == 'GET':
        form = PedidoForm()
    if form.is_valid():
        form.save()
        return redirect ('pedidos:pedido_list')
    return render(request, 'pedidos/pedido_create.html', {'form': form})

def pedido_update(request, pk: int):
    query = Pedido.objects.get(id=pk)
    if request.method == 'GET':
        form = PedidoForm(instance=query)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('pedidos:pedido_list')
    return render(request, 'pedidos/pedido_create.html', {'form': form})

 
def pedido_detail(request, pk: int):
    try:
        query = Pedido.objects.get(pk=pk)   
    except Pedido.DoesNotExist:
        messages.error(request, "No se encontró ningún pedido con ese número.")
        return redirect('pedidos:pedido_list')
    context = {'object': query}
    return render(request, 'pedidos/pedido_detail.html', context)
       
       
def buscar_pedido(request):
    if request.method == 'POST':
        numero_guia = request.POST.get('numero_guia')
        pedido = Pedido.objects.filter(id=numero_guia).first()
        if pedido:
            return redirect('pedidos:pedido_detail', pk=pedido.pk)   
        else:
            messages.error(request, "No se encontró ningún pedido con ese número.")
            return redirect('pedidos:pedido_list')
    return redirect('pedidos:pedido_list')