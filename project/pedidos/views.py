from django.shortcuts import render, redirect
from .models import Pedido
from .forms import PedidoForm
from django.db.models import Q


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
 