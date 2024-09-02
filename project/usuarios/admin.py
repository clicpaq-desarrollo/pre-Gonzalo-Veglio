from django.contrib import admin
from .models import Usuario 

#admin.site.register(Usuario)

@admin.register(Usuario)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("username","nombre","apellido", "email","fecha_creacion")
    list_filter = ("nombre","apellido" ) 
    search_fields = ("Usuario__nombre",) 
    ordering = ("-id",) 
    
 


     