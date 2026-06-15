import unittest
from vehiculos import consultar_disponibilidad
from database import inicializar_db


class TestVehiculos(unittest.TestCase):

    def setUp(self):
        inicializar_db()

    def test_consultar_disponibilidad(self):

        disponibles = consultar_disponibilidad(
            "2026-01-10",
            "2026-01-15"
        )

        self.assertIsInstance(disponibles, list)

        self.assertGreater(len(disponibles), 0)


if __name__ == "__main__":
    unittest.main()