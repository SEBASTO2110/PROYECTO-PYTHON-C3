import json
import os
from datetime import datetime
from herramientas import buscar, cargar as cargar_herr, actualizar_todas
from logs import registrar_log

ARCHIVO = "prestamos.json"


def cargar():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        return json.load(f)


def guardar(datos):
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)


def solicitar(id_p, id_usuario, id_herramienta, cantidad, fecha_devolucion, observaciones=""):
    prestamos = cargar()
    herramienta = buscar(id_herramienta)

    if not herramienta:
        return False, "Herramienta no existe"

    if herramienta["cantidad"] < cantidad:
        registrar_log("Intento de préstamo sin stock suficiente")
        return False, "No hay suficiente stock"

    nuevo = {
        "id": id_p,
        "usuario": id_usuario,
        "herramienta": id_herramienta,
        "cantidad": cantidad,
        "fecha_inicio": datetime.now().strftime("%Y-%m-%d"),
        "fecha_devolucion": fecha_devolucion,
        "estado": "pendiente",
        "observaciones": observaciones
    }

    prestamos.append(nuevo)
    guardar(prestamos)
    registrar_log(f"Solicitud creada: {id_p}")
    return True, "Solicitud creada"


def aprobar(id_p):
    prestamos = cargar()
    herramientas = cargar_herr()

    for p in prestamos:
        if p["id"] == id_p and p["estado"] == "pendiente":

            for h in herramientas:
                if h["id"] == p["herramienta"]:

                    if h["cantidad"] >= p["cantidad"]:
                        h["cantidad"] -= p["cantidad"]
                        h["veces_prestada"] += 1
                        p["estado"] = "activo"

                        actualizar_todas(herramientas)
                        guardar(prestamos)
                        registrar_log(f"Préstamo aprobado: {id_p}")
                        return True

    return False


def devolver(id_p):
    prestamos = cargar()
    herramientas = cargar_herr()

    for p in prestamos:
        if p["id"] == id_p and p["estado"] == "activo":

            for h in herramientas:
                if h["id"] == p["herramienta"]:
                    h["cantidad"] += p["cantidad"]
                    p["estado"] = "devuelto"

                    actualizar_todas(herramientas)
                    guardar(prestamos)
                    registrar_log(f"Préstamo devuelto: {id_p}")
                    return True

    return False


def listar():
    return cargar()
