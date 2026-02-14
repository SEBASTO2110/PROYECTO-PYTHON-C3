# Sistema Comunitario de Préstamo de Herramientas

## Descripción del Proyecto

Este proyecto consiste en un sistema desarrollado en Python que funciona en consola y permite gestionar el préstamo de herramientas entre los vecinos de una comunidad.

La idea principal es organizar el registro de herramientas, usuarios y préstamos para evitar pérdidas, confusiones o falta de control en el inventario.

El sistema guarda la información en archivos JSON para que los datos no se pierdan al cerrar el programa.



## Objetivo

Permitir que la junta comunal pueda:

- Registrar herramientas
- Registrar usuarios (administradores y residentes)
- Gestionar solicitudes de préstamo
- Aprobar préstamos
- Controlar la cantidad disponible de herramientas
- Registrar eventos importantes en un archivo de logs



## Tipos de Usuario

### Administrador

Puede:
- Crear herramientas
- Listar herramientas
- Aprobar préstamos solicitados
- Ver reportes
- Gestionar usuarios

### Residente

Puede:
- Consultar herramientas disponibles
- Solicitar préstamos
- Devolver herramientas



## Estructura del Proyecto

El proyecto está dividido en los siguientes archivos:

- main.py → Controla el menú principal y la interacción con el usuario
- usuarios.py → Gestiona la creación y búsqueda de usuarios
- herramientas.py → Gestiona las herramientas
- prestamos.py → Controla las solicitudes, aprobación y devolución de préstamos
- reportes.py → Genera reportes básicos del sistema
- logs.py → Guarda los eventos importantes en un archivo de texto

Archivos generados automáticamente:

- usuarios.json
- herramientas.json
- prestamos.json
- logs.txt



## Requisitos

- Python 3 instalado
- No se requieren librerías externas



## Cómo ejecutar el programa

1. Abrir la terminal en la carpeta del proyecto.
2. Ejecutar el siguiente comando:

python3 main.py

3. Seguir las instrucciones del menú.



## Funcionamiento General

1. Primero se debe crear un usuario administrador.
2. Luego el administrador puede crear herramientas.
3. Se pueden crear usuarios residentes.
4. El residente puede solicitar préstamos.
5. El administrador debe aprobar la solicitud.
6. Cuando el usuario devuelve la herramienta, el sistema actualiza el stock.



## Persistencia de Datos

El sistema utiliza archivos JSON para guardar la información, por lo tanto los datos permanecen almacenados incluso después de cerrar el programa.

