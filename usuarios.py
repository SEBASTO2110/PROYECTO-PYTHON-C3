import json
import os

ARCHIVO = "usuarios.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)


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
    return nuevo, "Usuario creado correctamente"


def listar():
    return cargar()


def buscar(id_usuario):
    usuarios = cargar()
    for u in usuarios:
        if u["id"] == id_usuario:
            return u
    return None
