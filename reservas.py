from datetime import datetime
from database import get_connection
from vehiculos import buscar_vehiculo, actualizar_estado, consultar_disponibilidad


def calcular_dias(fecha_inicio, fecha_fin):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    dias = (fin - inicio).days + 1

    return dias


def crear_reserva(id_vehiculo, cliente, fecha_inicio, fecha_fin):
    vehiculo = buscar_vehiculo(id_vehiculo)

    if not vehiculo:
        print("ERROR: Vehículo no encontrado.")
        return

    if vehiculo["estado"] != "Disponible":
        print(f"ERROR: El vehículo no está disponible. Estado actual: {vehiculo['estado']}")
        return

    if fecha_fin <= fecha_inicio:
        print("ERROR: La fecha de fin debe ser mayor a la de inicio.")
        return

    disponibles = consultar_disponibilidad(fecha_inicio, fecha_fin)
    ids_disponibles = [v["id"] for v in disponibles]

    if id_vehiculo not in ids_disponibles:
        print("ERROR: El vehículo ya tiene una reserva en esas fechas.")
        return

    dias = calcular_dias(fecha_inicio, fecha_fin)
    precio_dia = vehiculo["precio_dia"]
    total = dias * precio_dia

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reservas
        (id_vehiculo, cliente, fecha_inicio, fecha_fin, total)
        VALUES (?, ?, ?, ?, ?)
        """,
        (id_vehiculo, cliente, fecha_inicio, fecha_fin, total)
    )

    conn.commit()
    conn.close()

    actualizar_estado(id_vehiculo, "Alquilado")

    print(f"✔ Reserva registrada exitosamente para {cliente}.")
    print(f"  Vehículo      : {vehiculo['marca']} {vehiculo['modelo']}")
    print(f"  Días          : {dias}")
    print(f"  Precio por día: ${precio_dia:.2f}")
    print(f"  Total a pagar : ${total:.2f}")


def listar_reservas():
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
    """)

    reservas = cursor.fetchall()
    conn.close()

    print("\n--- RESERVAS REGISTRADAS ---")

    if not reservas:
        print("No hay reservas registradas.")
        return

    for r in reservas:
        print(f"  Reserva #{r['id']}")
        print(f"    Cliente : {r['cliente']}")
        print(f"    Vehículo: {r['marca']} {r['modelo']}")
        print(f"    Desde   : {r['fecha_inicio']}")
        print(f"    Hasta   : {r['fecha_fin']}")
        print(f"    Total   : ${r['total']:.2f}")
        print("  -------------------------")


def cancelar_reserva(id_reserva):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM reservas WHERE id = ?",
        (id_reserva,)
    )

    reserva = cursor.fetchone()

    if not reserva:
        print("ERROR: Reserva no encontrada.")
        conn.close()
        return

    cursor.execute(
        "DELETE FROM reservas WHERE id = ?",
        (id_reserva,)
    )

    conn.commit()
    conn.close()

    actualizar_estado(reserva["id_vehiculo"], "Disponible")

    print("✔ Reserva cancelada. Vehículo liberado.")


def buscar_reservas_por_cliente(nombre_cliente):
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
        WHERE LOWER(r.cliente) LIKE LOWER(?)
    """, (f"%{nombre_cliente}%",))

    reservas = cursor.fetchall()
    conn.close()

    print(f"\n--- RESERVAS PARA: '{nombre_cliente}' ---")

    if not reservas:
        print("  No se encontraron reservas para ese cliente.")
        return

    for r in reservas:
        print(f"  Reserva #{r['id']}")
        print(f"    Cliente : {r['cliente']}")
        print(f"    Vehículo: {r['marca']} {r['modelo']}")
        print(f"    Desde   : {r['fecha_inicio']}")
        print(f"    Hasta   : {r['fecha_fin']}")
        print(f"    Total   : ${r['total']:.2f}")
        print("  -------------------------")