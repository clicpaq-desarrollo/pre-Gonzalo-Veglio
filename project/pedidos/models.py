from django.db import models
from clientes.models import Cliente
from usuarios.models import Usuario

class Pedido(models.Model):
    class Estado(models.TextChoices):
        CREADO = 'Creado', 'Creado'
        RECIBIDO = 'Recibido', 'Recibido'
        EN_CAMINO = 'En camino', 'En camino'
        ENTREGADO = 'Entregado', 'Entregado'
    # Relaciones con los modelos Cliente y Usuario
    razon_social = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    # Datos personales de la persona que recibe el pedido
    nombre_destinatario = models.CharField(max_length=100)
    apellido_destinatario = models.CharField(max_length=100)
    telefono_destinatario = models.CharField(max_length=20)
    email_destinatario = models.EmailField()

    # Detalles de entrega
    direccion_entrega = models.CharField(max_length=200)
    ciudad_entrega = models.CharField(max_length=100)
    provincia_entrega = models.CharField(max_length=100)
    codigo_postal_entrega = models.CharField(max_length=20)

    # Detalles del pedido
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.CREADO)
    
    # Fecha de creación del pedido
    creado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Pedido  para {self.razon_social}"

