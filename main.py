# main.py
from database import inicializar_db
from vehiculos import listar_vehiculos, consultar_disponibilidad
from reservas import crear_reserva, listar_reservas, cancelar_reserva

def menu():
    inicializar_db()

    while True:
        print("\n=========================================")
        print("    SISTEMA DE ALQUILER DE VEHÍCULOS")
        print("=========================================")
        print("  1. Ver todos los vehículos")
        print("  2. Consultar disponibilidad")
        print("  3. Registrar nueva reserva")
        print("  4. Ver todas las reservas")
        print("  5. Cancelar una reserva")
        print("  6. Salir")
        print("-----------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_vehiculos()

        elif opcion == "2":
            print("\n--- CONSULTAR DISPONIBILIDAD ---")
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin    = input("Fecha de fin    (YYYY-MM-DD): ").strip()
            disponibles  = consultar_disponibilidad(fecha_inicio, fecha_fin)
            print("\n-----------------------------------------")
            if disponibles:
                print("  Vehículos disponibles:")
                for v in disponibles:
                    print(f"  ID: {v['id']} | {v['marca']} {v['modelo']}")
            else:
                print("  No hay vehículos disponibles en esas fechas.")
            print("-----------------------------------------")

        elif opcion == "3":
            print("\n--- NUEVA RESERVA ---")
            cliente      = input("Nombre del cliente: ").strip()
            id_vehiculo  = int(input("ID del vehículo: "))
            fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
            fecha_fin    = input("Fecha de fin    (YYYY-MM-DD): ").strip()
            crear_reserva(id_vehiculo, cliente, fecha_inicio, fecha_fin)

        elif opcion == "4":
            listar_reservas()

        elif opcion == "5":
            listar_reservas()
            id_reserva = int(input("\nNúmero de reserva a cancelar: "))
            cancelar_reserva(id_reserva)

        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()