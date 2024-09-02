# pre-Gonzalo-Veglio

# OptLog

OptLog es un sistema de Optimización Logística que facilita la gestión de envíos dentro de una red logística. El sistema permite manejar datos de clientes y realizar un seguimiento de los envíos realizados a distintos destinatarios.

## Descripción

OptLog es una aplicación desarrollada en Django que proporciona una solución para gestionar la logística de envíos. Incluye varias aplicaciones Django que cubren diferentes aspectos del sistema:

- **Clientes**: Manejo de datos de los clientes.
- **Geolocalización**: Información sobre la ubicación.
- **Pedidos**: Gestión de pedidos y su estado.
- **Usuarios**: Administración de usuarios y permisos.

Cada aplicación ofrece funciones CRUD (Crear, Leer, Actualizar, Eliminar) para su respectivo dominio.

## Funcionalidades en Desarrollo

Actualmente, el proyecto está en proceso de desarrollo y se están trabajando en las siguientes mejoras:

- **Desplegables para Provincias y Localidades**:
  - En los formularios de creación para clientes y pedidos, se añadirá un campo desplegable que permitirá seleccionar la **provincia** y la **localidad** correspondientes. Esto facilitará la selección de ubicaciones de manera más eficiente.

- **Sistema de Autenticación y Autorización**:
  - Se implementará un sistema de **login** que incluirá **permisos y roles**. Esta funcionalidad permitirá gestionar el acceso a diferentes partes de la aplicación de acuerdo con el rol del usuario, mejorando la seguridad y la administración de la aplicación.

- **Dependencia Dinámica de Localidades**:
  - Los formularios de creación para clientes y pedidos serán mejorados para permitir la selección de una **provincia** primero. Una vez seleccionada la provincia, se mostrarán únicamente las localidades correspondientes a esa provincia, simplificando el proceso de selección.

Estas características están en desarrollo y se implementarán en versiones futuras para mejorar la funcionalidad y la experiencia del usuario.

**CORRECCIONES ANTES DE LA ENTREGA** 

## Panel administrador
-usuario: admin
-Contraseña: 1234