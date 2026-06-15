from database import get_connection


def reporte_vehiculos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT estado, COUNT(*) AS cantidad
        FROM vehiculos
        GROUP BY estado
    """)

    datos = cursor.fetchall()
    conn.close()

    print("\n--- REPORTE DE VEHÍCULOS POR ESTADO ---")

    if not datos:
        print("No hay vehículos registrados.")
        return

    for d in datos:
        print(f"{d['estado']}: {d['cantidad']} vehículo(s)")


def reporte_reservas():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            r.id,
            r.cliente,
            v.marca,
            v.modelo,
            r.fecha_inicio,
            r.fecha_fin,
            r.total
        FROM reservas r
        JOIN vehiculos v ON r.id_vehiculo = v.id
        ORDER BY r.id DESC
    """)

    reservas = cursor.fetchall()
    conn.close()

    print("\n--- REPORTE GENERAL DE RESERVAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for r in reservas:
        print(f"Reserva #{r['id']}")
        print(f"Cliente : {r['cliente']}")
        print(f"Vehículo: {r['marca']} {r['modelo']}")
        print(f"Desde   : {r['fecha_inicio']}")
        print(f"Hasta   : {r['fecha_fin']}")
        print(f"Total   : ${r['total']:.2f}")
        print("-----------------------------")


def reporte_ingresos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            COUNT(*) AS total_reservas,
            SUM(total) AS ingresos_totales
        FROM reservas
    """)

    datos = cursor.fetchone()
    conn.close()

    print("\n--- REPORTE DE INGRESOS ---")

    total_reservas = datos["total_reservas"]
    ingresos = datos["ingresos_totales"]

    if ingresos is None:
        ingresos = 0

    print(f"Total de reservas : {total_reservas}")
    print(f"Ingresos totales  : ${ingresos:.2f}")


def menu_reportes():
    while True:
        print("\n=========================================")
        print("              MÓDULO DE REPORTES")
        print("=========================================")
        print("1. Reporte de vehículos por estado")
        print("2. Reporte general de reservas")
        print("3. Reporte de ingresos")
        print("4. Volver al menú principal")
        print("-----------------------------------------")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            reporte_vehiculos()

        elif opcion == "2":
            reporte_reservas()

        elif opcion == "3":
            reporte_ingresos()

        elif opcion == "4":
            break

        else:
            print("Opción inválida.")

        input("\nPresione Enter para continuar...")