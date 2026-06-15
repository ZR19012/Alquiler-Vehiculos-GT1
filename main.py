# main.py
import os
from datetime import datetime
from database import inicializar_db
from vehiculos import listar_vehiculos, consultar_disponibilidad, agregar_vehiculo
from reservas import crear_reserva, listar_reservas, cancelar_reserva


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


def menu():
    inicializar_db()

    while True:
        limpiar_pantalla()

        print("\n=========================================")
        print("    SISTEMA DE ALQUILER DE VEHÍCULOS")
        print("=========================================")
        print("  1. Ver todos los vehículos")
        print("  2. Consultar disponibilidad")
        print("  3. Registrar nueva reserva")
        print("  4. Ver todas las reservas")
        print("  5. Cancelar una reserva")
        print("  6. Agregar nuevo vehículo")
        print("  7. Salir")
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
            fecha_fin = input("Fecha de fin    (YYYY-MM-DD): ").strip()

            if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                print("\nERROR: Formato de fecha inválido. Use YYYY-MM-DD.")
                pausa()
                continue

            disponibles = consultar_disponibilidad(fecha_inicio, fecha_fin)

            print("\n-----------------------------------------")
            if disponibles:
                print("  Vehículos disponibles:")
                for v in disponibles:
                    print(f"  ID: {v['id']} | {v['marca']} {v['modelo']}")
            else:
                print("  No hay vehículos disponibles en esas fechas.")
            print("-----------------------------------------")
            pausa()

        elif opcion == "3":
            limpiar_pantalla()
            print("\n--- NUEVA RESERVA ---")
            cliente = input("Nombre del cliente: ").strip()

            try:
                id_vehiculo = int(input("ID del vehículo: ").strip())
            except ValueError:
                print("ERROR: El ID debe ser un número entero.")
                pausa()
                continue

            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin = input("Fecha de fin    (YYYY-MM-DD): ").strip()

            if not validar_fecha(fecha_inicio) or not validar_fecha(fecha_fin):
                print("\nERROR: Formato de fecha inválido. Use YYYY-MM-DD.")
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
                print("ERROR: El número de reserva debe ser un entero.")
                pausa()
                continue

            cancelar_reserva(id_reserva)
            pausa()

        elif opcion == "6":
            limpiar_pantalla()
            print("\n--- AGREGAR NUEVO VEHÍCULO ---")
            marca = input("Marca del vehículo: ").strip()
            modelo = input("Modelo del vehículo: ").strip()
            if not marca or not modelo:
                print("ERROR: La marca y el modelo no pueden estar vacíos.")
            else:
                agregar_vehiculo(marca, modelo)
            pausa()

        elif opcion == "7":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente de nuevo.")
            pausa()


if __name__ == "__main__":
    menu()