from database import get_connection


def listar_vehiculos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, marca, modelo, estado, precio_dia FROM vehiculos")
    vehiculos = cursor.fetchall()

    conn.close()

    print("\n--- LISTADO DE VEHÍCULOS ---")
    print(f"{'ID':<6} {'Marca':<10} {'Modelo':<12} {'Estado':<18} {'Precio/Día'}")
    print("-" * 65)

    for v in vehiculos:
        print(
            f"{v['id']:<6} "
            f"{v['marca']:<10} "
            f"{v['modelo']:<12} "
            f"{v['estado']:<18} "
            f"${v['precio_dia']:.2f}"
        )

    print("-" * 65)


def consultar_disponibilidad(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT v.id, v.marca, v.modelo, v.precio_dia
        FROM vehiculos v
        WHERE v.estado = 'Disponible'
        AND v.id NOT IN (
            SELECT r.id_vehiculo
            FROM reservas r
            WHERE NOT (r.fecha_fin < ? OR r.fecha_inicio > ?)
        )
    """, (fecha_inicio, fecha_fin))

    disponibles = cursor.fetchall()

    conn.close()

    return disponibles


def actualizar_estado(id_vehiculo, nuevo_estado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE vehiculos SET estado = ? WHERE id = ?",
        (nuevo_estado, id_vehiculo)
    )

    conn.commit()
    conn.close()


def cambiar_estado_vehiculo(id_vehiculo, nuevo_estado):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM vehiculos WHERE id = ?",
        (id_vehiculo,)
    )

    vehiculo = cursor.fetchone()

    if vehiculo is None:
        print("ERROR: No existe un vehículo con ese ID.")
        conn.close()
        return

    cursor.execute(
        "UPDATE vehiculos SET estado = ? WHERE id = ?",
        (nuevo_estado, id_vehiculo)
    )

    conn.commit()
    conn.close()

    print(f"✔ Estado actualizado correctamente a: {nuevo_estado}")


def buscar_vehiculo(id_vehiculo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM vehiculos WHERE id = ?",
        (id_vehiculo,)
    )

    vehiculo = cursor.fetchone()

    conn.close()

    return vehiculo


def agregar_vehiculo(marca, modelo, precio_dia):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id) FROM vehiculos")
    resultado = cursor.fetchone()[0]

    if resultado:
        nuevo_id = resultado + 1
    else:
        nuevo_id = 101

    cursor.execute(
        """
        INSERT INTO vehiculos
        (id, marca, modelo, estado, precio_dia)
        VALUES (?, ?, ?, ?, ?)
        """,
        (nuevo_id, marca, modelo, "Disponible", precio_dia)
    )

    conn.commit()
    conn.close()

    print(f"✔ Vehículo agregado exitosamente con ID {nuevo_id}.")


def eliminar_vehiculo(id_vehiculo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM vehiculos WHERE id = ?",
        (id_vehiculo,)
    )

    vehiculo = cursor.fetchone()

    if not vehiculo:
        print("ERROR: Vehículo no encontrado.")
        conn.close()
        return

    cursor.execute(
        "SELECT COUNT(*) FROM reservas WHERE id_vehiculo = ?",
        (id_vehiculo,)
    )

    total_reservas = cursor.fetchone()[0]

    if total_reservas > 0:
        print(
            f"ERROR: No se puede eliminar. "
            f"El vehículo tiene {total_reservas} reserva(s) activa(s)."
        )
        conn.close()
        return

    cursor.execute(
        "DELETE FROM vehiculos WHERE id = ?",
        (id_vehiculo,)
    )

    conn.commit()
    conn.close()

    print(f"✔ Vehículo ID {id_vehiculo} eliminado exitosamente.")