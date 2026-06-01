import sqlite3
import os

DB_PATH = os.path.join("data", "alquiler.db")

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id      INTEGER PRIMARY KEY,
            marca   TEXT NOT NULL,
            modelo  TEXT NOT NULL,
            estado  TEXT NOT NULL DEFAULT 'Disponible'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            id_vehiculo  INTEGER NOT NULL,
            cliente      TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin    TEXT NOT NULL,
            FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id)
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM vehiculos")
    if cursor.fetchone()[0] == 0:
        vehiculos_iniciales = [
            (101, "Toyota",  "Corolla", "Disponible"),
            (102, "Honda",   "Civic",   "Alquilado"),
            (103, "Nissan",  "Sentra",  "Disponible"),
            (104, "Ford",    "Mustang", "En Mantenimiento"),
            (105, "Kia",     "Rio",     "Disponible"),
        ]
        cursor.executemany(
            "INSERT INTO vehiculos (id, marca, modelo, estado) VALUES (?, ?, ?, ?)",
            vehiculos_iniciales
        )

    conn.commit()
    conn.close()