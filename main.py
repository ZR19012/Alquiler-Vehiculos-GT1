# ================================================
# SISTEMA DE ALQUILER DE VEHICULOS
# Proyecto Final - Logica de Programacion
# GT1 - Entrega 2
# ================================================

vehiculos = [
    {"id": 101, "marca": "Toyota", "modelo": "Corolla", "estado": "Disponible"},
    {"id": 102, "marca": "Honda", "modelo": "Civic", "estado": "Alquilado"},
    {"id": 103, "marca": "Nissan", "modelo": "Sentra", "estado": "Disponible"},
    {"id": 104, "marca": "Ford", "modelo": "Mustang", "estado": "En Mantenimiento"},
    {"id": 105, "marca": "Kia", "modelo": "Rio", "estado": "Disponible"}
]

reservas = [
    {"id_vehiculo": 101, "cliente": "Carlos Perez", "fecha_inicio": 20250110, "fecha_fin": 20250115},
    {"id_vehiculo": 103, "cliente": "Ana Gonzalez", "fecha_inicio": 20250120, "fecha_fin": 20250125}
]


def verificar_disponibilidad(fecha_ini_solicitud, fecha_fin_solicitud, fecha_ini_reserva, fecha_fin_reserva):
    if fecha_fin_solicitud < fecha_ini_reserva or fecha_ini_solicitud > fecha_fin_reserva:
        return True
    else:
        return False


def buscar_vehiculo(id_buscado):
    for vehiculo in vehiculos:
        if vehiculo["id"] == id_buscado:
            return vehiculo
    return None


def vehiculo_disponible_en_fechas(id_vehiculo, fecha_inicio, fecha_fin):
    for reserva in reservas:
        if reserva["id_vehiculo"] == id_vehiculo:
            disponible = verificar_disponibilidad(
                fecha_inicio,
                fecha_fin,
                reserva["fecha_inicio"],
                reserva["fecha_fin"]
            )

            if disponible == False:
                return False

    return True


def consultar_disponibilidad():
    print("\n--- CONSULTAR DISPONIBILIDAD ---")

    try:
        fecha_inicio = int(input("Fecha de inicio (AAAAMMDD): "))
        fecha_fin = int(input("Fecha de fin    (AAAAMMDD): "))

        if fecha_fin <= fecha_inicio:
            print("ERROR: La fecha de fin debe ser mayor a la fecha de inicio.")
            return

        print("\nVehiculos disponibles para esas fechas:")
        print("-----------------------------------------")

        hay_disponibles = False

        for vehiculo in vehiculos:
            if vehiculo["estado"] == "Disponible":
                if vehiculo_disponible_en_fechas(vehiculo["id"], fecha_inicio, fecha_fin):
                    print(f'ID: {vehiculo["id"]} | {vehiculo["marca"]} {vehiculo["modelo"]}')
                    hay_disponibles = True

        if hay_disponibles == False:
            print("No hay vehiculos disponibles para esas fechas.")

    except ValueError:
        print("ERROR: Debe ingresar las fechas en formato numerico. Ejemplo: 20250520")


def registrar_reserva():
    print("\n--- REGISTRAR NUEVA RESERVA ---")

    cliente = input("Nombre del cliente: ")

    try:
        id_vehiculo = int(input("ID del vehiculo a reservar: "))
        vehiculo = buscar_vehiculo(id_vehiculo)

        if vehiculo == None:
            print("ERROR: Vehiculo no encontrado.")
            return

        if vehiculo["estado"] != "Disponible":
            print("ERROR: El vehiculo no esta disponible.")
            print("Estado actual:", vehiculo["estado"])
            return

        fecha_inicio = int(input("Fecha de inicio (AAAAMMDD): "))
        fecha_fin = int(input("Fecha de fin    (AAAAMMDD): "))

        if fecha_fin <= fecha_inicio:
            print("ERROR: La fecha de fin debe ser mayor a la fecha de inicio.")
            return

        if vehiculo_disponible_en_fechas(id_vehiculo, fecha_inicio, fecha_fin):
            nueva_reserva = {
                "id_vehiculo": id_vehiculo,
                "cliente": cliente,
                "fecha_inicio": fecha_inicio,
                "fecha_fin": fecha_fin
            }

            reservas.append(nueva_reserva)
            vehiculo["estado"] = "Alquilado"

            print("Reserva registrada exitosamente.")
            print("Cliente:", cliente)
            print("Vehiculo:", vehiculo["marca"], vehiculo["modelo"])

        else:
            print("ERROR: El vehiculo ya tiene una reserva en esas fechas.")

    except ValueError:
        print("ERROR: Debe ingresar datos numericos donde corresponde.")


def ver_reservas():
    print("\n--- RESERVAS REGISTRADAS ---")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
    else:
        contador = 1

        for reserva in reservas:
            print(f"\nReserva #{contador}")
            print("Cliente :", reserva["cliente"])
            print("Vehiculo: ID", reserva["id_vehiculo"])
            print("Desde   :", reserva["fecha_inicio"])
            print("Hasta   :", reserva["fecha_fin"])
            print("-------------------------")
            contador += 1


def cancelar_reserva():
    print("\n--- CANCELAR RESERVA ---")

    if len(reservas) == 0:
        print("No hay reservas para cancelar.")
        return

    ver_reservas()

    try:
        numero = int(input("Numero de reserva a cancelar: "))

        if numero < 1 or numero > len(reservas):
            print("ERROR: Numero de reserva invalido.")
            return

        reserva_cancelada = reservas.pop(numero - 1)

        vehiculo = buscar_vehiculo(reserva_cancelada["id_vehiculo"])

        if vehiculo != None:
            vehiculo["estado"] = "Disponible"

        print("Reserva cancelada correctamente.")
        print("El vehiculo fue liberado.")

    except ValueError:
        print("ERROR: Debe ingresar un numero valido.")


def ver_vehiculos():
    print("\n--- LISTADO DE VEHICULOS ---")

    for vehiculo in vehiculos:
        print(f'ID: {vehiculo["id"]} | {vehiculo["marca"]} {vehiculo["modelo"]} | Estado: {vehiculo["estado"]}')


def menu_principal():
    opcion = 0

    while opcion != 6:
        print("\n=========================================")
        print("    SISTEMA DE ALQUILER DE VEHICULOS")
        print("=========================================")
        print("1. Consultar disponibilidad")
        print("2. Registrar nueva reserva")
        print("3. Ver todas las reservas")
        print("4. Cancelar una reserva")
        print("5. Ver vehiculos")
        print("6. Salir")
        print("-----------------------------------------")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                consultar_disponibilidad()
            elif opcion == 2:
                registrar_reserva()
            elif opcion == 3:
                ver_reservas()
            elif opcion == 4:
                cancelar_reserva()
            elif opcion == 5:
                ver_vehiculos()
            elif opcion == 6:
                print("Saliendo del sistema. Hasta luego!")
            else:
                print("Opcion invalida. Intente de nuevo.")

        except ValueError:
            print("ERROR: Debe ingresar una opcion numerica.")


menu_principal()