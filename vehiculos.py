from database import get_connection

def listar_vehiculos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, marca, modelo, estado FROM vehiculos")
    vehiculos = cursor.fetchall()
    conn.close()

    print("\n--- LISTADO DE VEHÍCULOS ---")
    print(f"{'ID':<6} {'Marca':<10} {'Modelo':<12} {'Estado'}")
    print("-" * 42)
    for v in vehiculos:
        print(f"{v['id']:<6} {v['marca']:<10} {v['modelo']:<12} {v['estado']}")
    print("-" * 42)

def consultar_disponibilidad(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.id, v.marca, v.modelo
        FROM vehiculos v
        WHERE v.estado = 'Disponible'
        AND v.id NOT IN (
            SELECT r.id_vehiculo FROM reservas r
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

def buscar_vehiculo(id_vehiculo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vehiculos WHERE id = ?", (id_vehiculo,))
    vehiculo = cursor.fetchone()
    conn.close()
    return vehiculo

def agregar_vehiculo(marca, modelo):
    """Agrega un nuevo vehículo al sistema."""
    conn = get_connection()
    cursor = conn.cursor()

    # Generar ID automático (el mayor ID existente + 1)
    cursor.execute("SELECT MAX(id) FROM vehiculos")
    resultado = cursor.fetchone()[0]
    nuevo_id = (resultado + 1) if resultado else 101

    cursor.execute(
        "INSERT INTO vehiculos (id, marca, modelo, estado) VALUES (?, ?, ?, ?)",
        (nuevo_id, marca, modelo, "Disponible")
    )
    conn.commit()
    conn.close()
    print(f"✔ Vehículo agregado exitosamente con ID {nuevo_id}.")

def eliminar_vehiculo(id_vehiculo):
    """Elimina un vehículo solo si no tiene reservas activas."""
    conn = get_connection()
    cursor = conn.cursor()

    # Verificar que el vehículo existe
    cursor.execute("SELECT * FROM vehiculos WHERE id = ?", (id_vehiculo,))
    vehiculo = cursor.fetchone()

    if not vehiculo:
        print("ERROR: Vehículo no encontrado.")
        conn.close()
        return

    # Verificar que no tenga reservas activas
    cursor.execute("SELECT COUNT(*) FROM reservas WHERE id_vehiculo = ?", (id_vehiculo,))
    total_reservas = cursor.fetchone()[0]

    if total_reservas > 0:
        print(f"ERROR: No se puede eliminar. El vehículo tiene {total_reservas} reserva(s) activa(s).")
        conn.close()
        return

    cursor.execute("DELETE FROM vehiculos WHERE id = ?", (id_vehiculo,))
    conn.commit()
    conn.close()
    print(f"✔ Vehículo ID {id_vehiculo} eliminado exitosamente.")