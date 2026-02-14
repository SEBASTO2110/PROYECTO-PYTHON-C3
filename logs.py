from datetime import datetime
import os

ARCHIVO = "logs.txt"


def registrar_log(mensaje):
    """
    Registra un evento o error en el archivo logs.txt
    """

    # Si el archivo no existe, lo crea automáticamente
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            f.write("=== REGISTRO DE EVENTOS DEL SISTEMA ===\n\n")

    # Agregar nuevo registro
    with open(ARCHIVO, "a") as f:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] {mensaje}\n")
