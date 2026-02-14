from usuarios import crear_usuario, buscar
from herramientas import crear, listar
from prestamos import solicitar, aprobar, devolver
from reportes import stock_bajo, prestamos_activos, herramientas_mas_solicitadas


def menu_inicio():
    print("\n===== SISTEMA COMUNITARIO =====")
    print("1. Ingresar como administrador")
    print("2. Ingresar como residente")
    print("3. Crear usuario")
    print("0. Salir")


def login(tipo):
    id_usuario = input("Ingrese su ID: ")
    usuario = buscar(id_usuario)

    if not usuario:
        print("Usuario no existe")
        return None

    if usuario["tipo"] != tipo:
        print("Tipo incorrecto")
        return None

    return usuario


def panel_admin(usuario):
    while True:
        print("\n===== PANEL ADMIN =====")
        print("1. Crear herramienta")
        print("2. Listar herramientas")
        print("3. Aprobar préstamo")
        print("4. Reportes")
        print("0. Salir")

        op = input("Seleccione: ")

        if op == "1":
            id_h = input("ID herramienta: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría : ")
            cantidad = int(input("Cantidad: "))
            estado = input("Estado (activa, en reparación, fuera de servicio): ")
            valor = float(input("Valor: "))
            if crear(id_h, nombre, categoria, cantidad, estado, valor):
                print("Herramienta creada")
            else:
                print("ID ya existe")

        elif op == "2":
            for h in listar():
                print(h)

        elif op == "3":
            id_p = input("ID préstamo: ")
            if aprobar(id_p):
                print("Préstamo aprobado")
            else:
                print("No se pudo aprobar")

        elif op == "4":
            print("Stock bajo:", stock_bajo())
            print("Préstamos activos:", prestamos_activos())
            print("Más solicitadas:", herramientas_mas_solicitadas())

        elif op == "0":
            break


def panel_usuario(usuario):
    while True:
        print("\n===== PANEL RESIDENTE =====")
        print("1. Ver herramientas")
        print("2. Solicitar préstamo")
        print("3. Devolver")
        print("0. Salir")

        op = input("Seleccione: ")

        if op == "1":
            for h in listar():
                print(h)

        elif op == "2":
            id_p = input("ID préstamo: ")
            id_h = input("ID herramienta: ")
            cantidad = int(input("Cantidad: "))
            ok, msg = solicitar(id_p, usuario["id"], id_h, cantidad)
            print(msg)

        elif op == "3":
            id_p = input("ID préstamo: ")
            if devolver(id_p):
                print("Devuelto correctamente")
            else:
                print("No se pudo devolver")

        elif op == "0":
            break


def main():
    while True:
        menu_inicio()
        opcion = input("Seleccione: ")

        if opcion == "1":
            usuario = login("administrador")
            if usuario:
                panel_admin(usuario)

        elif opcion == "2":
            usuario = login("residente")
            if usuario:
                panel_usuario(usuario)

        elif opcion == "3":
            id_usuario = input("Cree un ID: ")
            nombres = input("Nombres: ")
            apellidos = input("Apellidos: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")
            tipo = input("Tipo (administrador/residente): ").lower()
            usuario, msg = crear_usuario(
                id_usuario, nombres, apellidos, telefono, direccion, tipo
            )
            print(msg)

        elif opcion == "0":
            break


if __name__ == "__main__":
    main()
