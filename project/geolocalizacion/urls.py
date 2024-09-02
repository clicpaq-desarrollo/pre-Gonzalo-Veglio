from django.urls import path

from . import views

app_name = 'geolocalizacion'

urlpatterns = [  
    path('provincias/list', views.provincia_list, name='provincia_list'),
    path('provincias/create', views.provincia_create, name='provincia_create'),
    path('provincia/delete/<int:pk>',views.provincia_delete,name='provincia_delete'),
    path('provincia/update/<int:pk>',views.provincia_update,name='provincia_update'),

    path('localidades/list', views.localidad_list, name='localidad_list'),
    path('localidades/create', views.localidad_create, name='localidad_create'),
    path('localidad/delete/<int:pk>',views.localidad_delete,name='localidad_delete'),
    path('localidad/update/<int:pk>',views.localidad_update,name='localidad_update'),

]

