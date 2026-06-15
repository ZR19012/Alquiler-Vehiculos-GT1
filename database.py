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

            id INTEGER PRIMARY KEY,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'Disponible',
            precio_dia REAL NOT NULL DEFAULT 0

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_vehiculo INTEGER NOT NULL,
            cliente TEXT NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL,
            total REAL NOT NULL DEFAULT 0,

            FOREIGN KEY (id_vehiculo)
            REFERENCES vehiculos(id)

        )
    """)

    cursor.execute("SELECT COUNT(*) FROM vehiculos")

    cantidad = cursor.fetchone()[0]

    if cantidad == 0:

        vehiculos_iniciales = [

            (101, "Toyota", "Corolla", "Disponible", 25.00),
            (102, "Honda", "Civic", "Disponible", 28.00),
            (103, "Nissan", "Sentra", "Disponible", 24.00),
            (104, "Ford", "Mustang", "Disponible", 55.00),
            (105, "Kia", "Rio", "Disponible", 22.00)

        ]

        cursor.executemany(
            """
            INSERT INTO vehiculos
            (id, marca, modelo, estado, precio_dia)

            VALUES (?, ?, ?, ?, ?)
            """,
            vehiculos_iniciales
        )

    conn.commit()
    conn.close()