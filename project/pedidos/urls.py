from django.urls import path

from . import views

app_name = 'pedidos'


urlpatterns = [
    path('', views.index, name='index'), 
    path('pedido/list', views.pedido_list, name='pedido_list'),
    path('pedido/create', views.pedido_create, name='pedido_create'),
    path('pedido/update/<int:pk>',views.pedido_update,name='pedido_update'),

]