from django.urls import path

from . import views

app_name = 'clientes'


urlpatterns = [
    path('', views.index, name='index'), 
    path('clientes/list', views.cliente_list, name='cliente_list'),
    path('clientes/create', views.cliente_create, name='cliente_create'),
    path('cliente/delete/<int:pk>',views.cliente_delete,name='cliente_delete'),

]