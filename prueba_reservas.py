# prueba_reservas.py
# Cubre el modulo de reservas y reportes

import unittest
import os
from database import get_connection, inicializar_db, DB_PATH
from vehiculos import buscar_vehiculo
from reservas import crear_reserva, cancelar_reserva, calcular_dias
from reportes import reporte_ingresos


class TestReservas(unittest.TestCase):

    def setUp(self):
        """Crea una base de datos limpia antes de cada prueba."""
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)
        inicializar_db()

    def tearDown(self):
        """Elimina la base de datos de prueba despues de cada test."""
        if os.path.exists(DB_PATH):
            os.remove(DB_PATH)

    def test_calcular_dias(self):
        """Verifica que el calculo de dias entre fechas sea correcto."""
        dias = calcular_dias("2026-01-10", "2026-01-15")
        self.assertEqual(dias, 6)  # incluye ambos extremos

    def test_crear_reserva_calcula_total_correcto(self):
        """Verifica que el total se calcule como dias * precio_dia."""
        crear_reserva(101, "Maria Lopez", "2026-02-01", "2026-02-05")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT total FROM reservas WHERE cliente = 'Maria Lopez'")
        total = cursor.fetchone()["total"]
        conn.close()

        # Toyota Corolla (id 101) cuesta 25.00/dia, son 5 dias
        self.assertEqual(total, 125.00)

    def test_crear_reserva_actualiza_estado_vehiculo(self):
        """Verifica que el vehiculo pase a 'Alquilado' tras reservar."""
        crear_reserva(103, "Pedro Ramirez", "2026-03-01", "2026-03-03")
        vehiculo = buscar_vehiculo(103)
        self.assertEqual(vehiculo["estado"], "Alquilado")

    def test_no_se_crea_reserva_con_vehiculo_inexistente(self):
        """Verifica que no se inserte una reserva si el vehiculo no existe."""
        crear_reserva(999, "Cliente Fantasma", "2026-04-01", "2026-04-05")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM reservas WHERE id_vehiculo = 999")
        total = cursor.fetchone()[0]
        conn.close()

        self.assertEqual(total, 0)

    def test_cancelar_reserva_elimina_registro(self):
        """Verifica que cancelar una reserva la borre de la base de datos."""
        crear_reserva(104, "Luis Hernandez", "2026-05-01", "2026-05-02")

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM reservas WHERE cliente = 'Luis Hernandez'")
        id_reserva = cursor.fetchone()["id"]
        conn.close()

        cancelar_reserva(id_reserva)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM reservas WHERE id = ?", (id_reserva,))
        existe = cursor.fetchone()[0]
        conn.close()

        self.assertEqual(existe, 0)

    def test_reporte_ingresos_sin_reservas(self):
        """Verifica que el reporte de ingresos no falle si no hay reservas."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*), SUM(total) FROM reservas")
        total_reservas, ingresos = cursor.fetchone()
        conn.close()

        self.assertEqual(total_reservas, 0)
        self.assertIsNone(ingresos)

    def test_reporte_ingresos_con_reservas(self):
        """Verifica que el reporte de ingresos sume correctamente el total."""
        crear_reserva(105, "Ana Torres", "2026-06-01", "2026-06-03")  # Kia Rio $22/dia, 3 dias = 66

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(total) FROM reservas")
        ingresos = cursor.fetchone()[0]
        conn.close()

        self.assertEqual(ingresos, 66.00)


if __name__ == "__main__":
    unittest.main(verbosity=2)