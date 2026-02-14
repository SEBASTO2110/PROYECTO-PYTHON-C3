from herramientas import listar as listar_herr
from prestamos import listar as listar_prest


def stock_bajo():
    return [h for h in listar_herr() if h["cantidad"] < 3]


def prestamos_activos():
    return [p for p in listar_prest() if p["estado"] == "activo"]


def herramientas_mas_solicitadas():
    herramientas = listar_herr()
    herramientas.sort(key=lambda x: x["veces_prestada"], reverse=True)
    return herramientas

