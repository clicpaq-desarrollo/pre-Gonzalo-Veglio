from django.contrib import admin

from .models import Pedido

#admin.site.register(Pedido)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id","razon_social","nombre_destinatario","apellido_destinatario", "ciudad_entrega","provincia_entrega", "estado", "fecha_creacion")
    list_filter = ("estado", "id") 
    search_fields = ("cliente__razon_social","id") 
    ordering = ("-fecha_creacion", "id")
    date_hierarchy = "fecha_creacion"
    
    