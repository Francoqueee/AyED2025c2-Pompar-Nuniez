import unittest
from TrabajoPractico_2.modules import MonticuloAvanzado, Paciente, SalaDeEmergencias


class TestMonticuloMin(unittest.TestCase):
    """Pruebas unitarias para el TAD MonticuloMin."""

    def setUp(self):
        self.monticulo = MonticuloAvanzado("riesgo", "llegada")

    def test_insertar_y_eliminar_minimo(self):
        p1 = {"nombre": "Ana", "riesgo": 2, "llegada": 1}
        p2 = {"nombre": "Juan", "riesgo": 1, "llegada": 2}
        p3 = {"nombre": "Lucía", "riesgo": 1, "llegada": 3}

        self.monticulo.insertar(p1)
        self.monticulo.insertar(p2)
        self.monticulo.insertar(p3)

        # El mínimo debe ser Juan (riesgo=1, llegada=2)
        self.assertEqual(self.monticulo.eliminar_minimo()["nombre"], "Juan")
        # Luego Lucía
        self.assertEqual(self.monticulo.eliminar_minimo()["nombre"], "Lucía")
        # Finalmente Ana
        self.assertEqual(self.monticulo.eliminar_minimo()["nombre"], "Ana")

    def test_buscar_minimo_no_elimina(self):
        p1 = {"nombre": "Carlos", "riesgo": 3, "llegada": 1}
        p2 = {"nombre": "Laura", "riesgo": 1, "llegada": 2}

        self.monticulo.insertar(p1)
        self.monticulo.insertar(p2)

        minimo = self.monticulo.buscar_minimo()
        self.assertEqual(minimo["nombre"], "Laura")
        # Verificar que el tamaño no cambió
        self.assertEqual(self.monticulo.tamano(), 2)

    def test_esta_vacio(self):
        self.assertTrue(self.monticulo.esta_vacio())
        self.monticulo.insertar({"riesgo": 2})
        self.assertFalse(self.monticulo.esta_vacio())


class TestSalaDeEmergencias(unittest.TestCase):
    """Pruebas unitarias para la aplicación SalaDeEmergencias."""

    def setUp(self):
        self.sala = SalaDeEmergencias()

    def test_ingresar_y_atender_pacientes(self):
        self.sala.ingresar_paciente(Paciente("Ana", 2, 1))
        self.sala.ingresar_paciente(Paciente("Juan", 1, 2))
        self.sala.ingresar_paciente(Paciente("Lucía", 1, 3))

        self.assertEqual(self.sala.cantidad_pacientes(), 3)

        # Orden esperado de atención: Juan, Lucía, Ana
        orden_esperado = ["Juan", "Lucía", "Ana"]
        atendidos = []

        while self.sala.cantidad_pacientes() > 0:
            paciente = self.sala.monticulo.eliminar_minimo()
            # Si el montículo devuelve diccionarios o Paciente, manejamos ambos
            nombre = paciente["nombre"] if isinstance(paciente, dict) else paciente.nombre
            atendidos.append(nombre)

        self.assertEqual(atendidos, orden_esperado)

    def test_atender_con_sala_vacia(self):
        self.assertTrue(self.sala.monticulo.esta_vacio())
        # No debería lanzar error al intentar atender
        try:
            self.sala.atender_paciente()
        except Exception:
            self.fail("atender_paciente() lanzó una excepción inesperada.")


if __name__ == "__main__":
    unittest.main()
