from herramientas import listar as listar_herr
from prestamos import listar as listar_prest
from datetime import datetime


def stock_bajo():
    return [h for h in listar_herr() if h["cantidad"] < 3]


def prestamos_activos():
    return [p for p in listar_prest() if p["estado"] == "activo"]


def prestamos_vencidos():
    hoy = datetime.now().strftime("%Y-%m-%d")
    return [
        p for p in listar_prest()
        if p["estado"] == "activo" and p["fecha_devolucion"] < hoy
    ]


def historial_usuario(id_usuario):
    return [p for p in listar_prest() if p["usuario"] == id_usuario]


def herramientas_mas_solicitadas():
    herramientas = listar_herr()
    herramientas.sort(key=lambda x: x["veces_prestada"], reverse=True)
    return herramientas


def usuarios_mas_activos():
    prestamos = listar_prest()
    conteo = {}

    for p in prestamos:
        usuario = p["usuario"]
        conteo[usuario] = conteo.get(usuario, 0) + 1

    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)
