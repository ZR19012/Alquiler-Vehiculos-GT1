import os
from datetime import datetime
from database import inicializar_db
from vehiculos import (
    listar_vehiculos,
    consultar_disponibilidad,
    agregar_vehiculo,
    eliminar_vehiculo,
    cambiar_estado_vehiculo
)
from reservas import (
    crear_reserva,
    listar_reservas,
    cancelar_reserva,
    buscar_reservas_por_cliente
)
from reportes import menu_reportes


def limpiar_pantalla():
    os.system("cls")


def pausa():
    input("\nPresione Enter para continuar...")


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validar_rango_fechas(fecha_inicio, fecha_fin):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    return fin >= inicio


def menu():
    inicializar_db()

    while True:
        limpiar_pantalla()

        print("=========================================")
        print("    SISTEMA DE ALQUILER DE VEHÍCULOS")
        print("=========================================")
        print("1. Ver todos los vehículos")
        print("2. Consultar disponibilidad")
        print("3. Registrar nueva reserva")
        print("4. Ver todas las reservas")
        print("5. Cancelar una reserva")
        print("6. Agregar nuevo vehículo")
        print("7. Eliminar un vehículo")
        print("8. Buscar reservas por cliente")
        print("9. Cambiar estado de vehículo")
        print("10. Reportes")
        print("11. Salir")
        print("-----------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("\n--- LISTA DE VEHÍCULOS ---")
            listar_vehiculos()
            pausa()

        elif opcion == "2":
            limpiar_pantalla()
            print("\n--- CONSULTAR DISPONIBILIDAD ---")

            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()

            if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                print("\nERROR: Formato de fecha inválido.")
                pausa()
                continue

            if not validar_rango_fechas(fecha_inicio, fecha_fin):
                print("\nERROR: La fecha final no puede ser menor.")
                pausa()
                continue

            disponibles = consultar_disponibilidad(fecha_inicio, fecha_fin)

            print("\nVehículos disponibles:\n")

            if disponibles:
                for v in disponibles:
                    print(
                        f"ID: {v['id']} | "
                        f"{v['marca']} {v['modelo']} | "
                        f"${v['precio_dia']:.2f} por día"
                    )
            else:
                print("No hay vehículos disponibles.")

            pausa()

        elif opcion == "3":
            limpiar_pantalla()
            print("\n--- NUEVA RESERVA ---")

            cliente = input("Nombre del cliente: ").strip()

            if not cliente:
                print("ERROR: El nombre no puede estar vacío.")
                pausa()
                continue

            try:
                id_vehiculo = int(input("ID del vehículo: ").strip())
            except ValueError:
                print("ERROR: El ID debe ser numérico.")
                pausa()
                continue

            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha de fin (YYYY-MM-DD): ").strip()

            if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                print("\nERROR: Formato de fecha inválido.")
                pausa()
                continue

            if not validar_rango_fechas(fecha_inicio, fecha_fin):
                print("\nERROR: La fecha final no puede ser menor.")
                pausa()
                continue

            crear_reserva(id_vehiculo, cliente, fecha_inicio, fecha_fin)
            pausa()

        elif opcion == "4":
            limpiar_pantalla()
            print("\n--- LISTA DE RESERVAS ---")
            listar_reservas()
            pausa()

        elif opcion == "5":
            limpiar_pantalla()
            print("\n--- CANCELAR RESERVA ---")
            listar_reservas()

            try:
                id_reserva = int(input("\nNúmero de reserva a cancelar: ").strip())
            except ValueError:
                print("ERROR: Debe ingresar un número.")
                pausa()
                continue

            cancelar_reserva(id_reserva)
            pausa()

        elif opcion == "6":
            limpiar_pantalla()
            print("\n--- AGREGAR VEHÍCULO ---")

            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()

            if not marca or not modelo:
                print("ERROR: No deje campos vacíos.")
                pausa()
                continue

            try:
                precio_dia = float(input("Precio por día: $").strip())
            except ValueError:
                print("ERROR: El precio debe ser numérico.")
                pausa()
                continue

            if precio_dia <= 0:
                print("ERROR: El precio debe ser mayor a cero.")
                pausa()
                continue

            agregar_vehiculo(marca, modelo, precio_dia)
            pausa()

        elif opcion == "7":
            limpiar_pantalla()
            print("\n--- ELIMINAR VEHÍCULO ---")
            listar_vehiculos()

            try:
                id_vehiculo = int(input("\nID del vehículo a eliminar: ").strip())
            except ValueError:
                print("ERROR: El ID debe ser numérico.")
                pausa()
                continue

            eliminar_vehiculo(id_vehiculo)
            pausa()

        elif opcion == "8":
            limpiar_pantalla()
            print("\n--- BUSCAR RESERVAS POR CLIENTE ---")

            nombre = input("Nombre del cliente a buscar: ").strip()

            if not nombre:
                print("ERROR: El nombre no puede estar vacío.")
            else:
                buscar_reservas_por_cliente(nombre)

            pausa()

        elif opcion == "9":
            limpiar_pantalla()
            print("\n--- CAMBIAR ESTADO DE VEHÍCULO ---")

            listar_vehiculos()

            try:
                id_vehiculo = int(input("\nID del vehículo: ").strip())
            except ValueError:
                print("ERROR: El ID debe ser numérico.")
                pausa()
                continue

            print("\nEstados disponibles:")
            print("1. Disponible")
            print("2. Alquilado")
            print("3. En Mantenimiento")

            opcion_estado = input("Seleccione el nuevo estado: ").strip()

            if opcion_estado == "1":
                nuevo_estado = "Disponible"
            elif opcion_estado == "2":
                nuevo_estado = "Alquilado"
            elif opcion_estado == "3":
                nuevo_estado = "En Mantenimiento"
            else:
                print("ERROR: Estado inválido.")
                pausa()
                continue

            cambiar_estado_vehiculo(id_vehiculo, nuevo_estado)
            pausa()

        elif opcion == "10":
            limpiar_pantalla()
            menu_reportes()

        elif opcion == "11":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")
            pausa()


if __name__ == "__main__":
    menu()