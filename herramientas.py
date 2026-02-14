import json
import os

ARCHIVO = "herramientas.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)


def crear(id_h, nombre, categoria, cantidad, estado, valor):
    herramientas = cargar()

    for h in herramientas:
        if h["id"] == id_h:
            return False

    nueva = {
        "id": id_h,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "estado": estado,
        "valor": valor,
        "veces_prestada": 0
    }

    herramientas.append(nueva)
    guardar(herramientas)
    return True


def listar():
    return cargar()


def buscar(id_h):
    herramientas = cargar()
    for h in herramientas:
        if h["id"] == id_h:
            return h
    return None


def actualizar_todas(herramientas):
    guardar(herramientas)