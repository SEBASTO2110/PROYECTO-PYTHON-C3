import json
import os
from logs import registrar_log

ARCHIVO = "usuarios.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar(datos):
    with open(ARCHIVO, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def crear_usuario(id_usuario, nombres, apellidos, telefono, direccion, tipo):
    usuarios = cargar()

    for u in usuarios:
        if u["id"] == id_usuario:
            return None, "Error: ID ya existe"

    nuevo = {
        "id": id_usuario,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }

    usuarios.append(nuevo)
    guardar(usuarios)
    registrar_log(f"Usuario creado: {id_usuario}")
    return nuevo, "Usuario creado correctamente"


def listar():
    return cargar()


def buscar(id_usuario):
    usuarios = cargar()
    for u in usuarios:
        if u["id"] == id_usuario:
            return u
    return None


def actualizar_usuario(id_usuario, nuevos_datos):
    usuarios = cargar()

    for u in usuarios:
        if u["id"] == id_usuario:
            u.update(nuevos_datos)
            guardar(usuarios)
            registrar_log(f"Usuario actualizado: {id_usuario}")
            return True

    return False


def eliminar_usuario(id_usuario):
    usuarios = cargar()
    usuarios_filtrados = [u for u in usuarios if u["id"] != id_usuario]

    if len(usuarios) == len(usuarios_filtrados):
        return False

    guardar(usuarios_filtrados)
    registrar_log(f"Usuario eliminado: {id_usuario}")
    return True
