from django.contrib import admin
from .models import Provincia, Localidad ,Cliente

admin.site.register(Provincia)
admin.site.register(Localidad)
#admin.site.register(Cliente)

@admin.register(Cliente)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("razon_social","email","localidad", "email","provincia")
    list_filter = ("razon_social", ) 
    search_fields = ("Cliente__razon_social",) 
    ordering = ("-id",) 
    
    
 

