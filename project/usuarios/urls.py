from django.urls import path

from . import views

app_name = 'usuarios'


urlpatterns = [
    path('', views.index, name='index'), 
    path('usuarios/list', views.usuario_list, name='usuario_list'),
    path('usuarios/create', views.usuario_create, name='usuario_create'),
]