from usuarios import (
    crear_usuario,
    buscar,
    listar as listar_usuarios,
    actualizar_usuario,
    eliminar_usuario,
)

from herramientas import (
    crear,
    listar,
    actualizar_herramienta,
    eliminar_herramienta,
)

from prestamos import solicitar, aprobar, devolver
from reportes import (
    stock_bajo,
    prestamos_activos,
    prestamos_vencidos,
    historial_usuario,
    herramientas_mas_solicitadas,
    usuarios_mas_activos,
)


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
        print("3. Actualizar herramienta")
        print("4. Eliminar herramienta")
        print("5. Aprobar préstamo")
        print("6. Reportes")
        print("7. Gestionar usuarios")
        print("0. Salir")

        op = input("Seleccione: ")

        if op == "1":
            id_h = input("ID herramienta: ")
            nombre = input("Nombre: ")
            categoria = input("Categoría: ")
            cantidad = int(input("Cantidad: "))
            estado = input("Estado: ")
            valor = float(input("Valor: "))

            if crear(id_h, nombre, categoria, cantidad, estado, valor):
                print("Herramienta creada")
            else:
                print("ID ya existe")

        elif op == "2":
            for h in listar():
                print(h)

        elif op == "3":
            id_h = input("ID herramienta a actualizar: ")
            campo = input("Campo a modificar: ")
            nuevo_valor = input("Nuevo valor: ")
            if actualizar_herramienta(id_h, {campo: nuevo_valor}):
                print("Actualizada correctamente")
            else:
                print("No encontrada")

        elif op == "4":
            id_h = input("ID herramienta a eliminar: ")
            if eliminar_herramienta(id_h):
                print("Eliminada")
            else:
                print("No encontrada")

        elif op == "5":
            id_p = input("ID préstamo: ")
            if aprobar(id_p):
                print("Préstamo aprobado")
            else:
                print("No se pudo aprobar")

        elif op == "6":
            print("Stock bajo:", stock_bajo())
            print("Préstamos activos:", prestamos_activos())
            print("Préstamos vencidos:", prestamos_vencidos())
            print("Herramientas más solicitadas:", herramientas_mas_solicitadas())
            print("Usuarios más activos:", usuarios_mas_activos())

        elif op == "7":
            print("1. Listar usuarios")
            print("2. Actualizar usuario")
            print("3. Eliminar usuario")
            sub = input("Seleccione: ")

            if sub == "1":
                for u in listar_usuarios():
                    print(u)

            elif sub == "2":
                id_u = input("ID usuario: ")
                campo = input("Campo a modificar: ")
                nuevo_valor = input("Nuevo valor: ")
                if actualizar_usuario(id_u, {campo: nuevo_valor}):
                    print("Actualizado")
                else:
                    print("No encontrado")

            elif sub == "3":
                id_u = input("ID usuario: ")
                if eliminar_usuario(id_u):
                    print("Eliminado")
                else:
                    print("No encontrado")

        elif op == "0":
            break


def panel_usuario(usuario):
    while True:
        print("\n===== PANEL RESIDENTE =====")
        print("1. Ver herramientas")
        print("2. Solicitar préstamo")
        print("3. Devolver")
        print("4. Mi historial")
        print("0. Salir")

        op = input("Seleccione: ")

        if op == "1":
            for h in listar():
                print(h)

        elif op == "2":
            id_p = input("ID préstamo: ")
            id_h = input("ID herramienta: ")
            cantidad = int(input("Cantidad: "))
            fecha_dev = input("Fecha estimada devolución (YYYY-MM-DD): ")
            observaciones = input("Observaciones: ")

            ok, msg = solicitar(
                id_p,
                usuario["id"],
                id_h,
                cantidad,
                fecha_dev,
                observaciones,
            )
            print(msg)

        elif op == "3":
            id_p = input("ID préstamo: ")
            if devolver(id_p):
                print("Devuelto correctamente")
            else:
                print("No se pudo devolver")

        elif op == "4":
            print(historial_usuario(usuario["id"]))

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
