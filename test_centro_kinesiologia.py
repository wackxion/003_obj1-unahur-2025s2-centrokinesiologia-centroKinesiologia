import unittest

from aparatos import Bicicleta, Magneto, Minitramp
from pacientes import Paciente


class TestParte1AparatosYPacientes(unittest.TestCase):
    def crearLeonardo(self):
        return Paciente("Leonardo", 40, 20, 10)

    def crearMilena(self):
        return Paciente("Milena", 3, 50, 30)

    def test_quien_puede_usar_cada_aparato(self):
        leonardo = self.crearLeonardo()
        milena = self.crearMilena()

        magneto = Magneto()
        bicicleta = Bicicleta()
        minitramp = Minitramp()

        self.assertTrue(leonardo.puedeUsar(magneto))
        self.assertTrue(leonardo.puedeUsar(bicicleta))
        self.assertTrue(leonardo.puedeUsar(minitramp))

        self.assertTrue(milena.puedeUsar(magneto))
        self.assertFalse(milena.puedeUsar(bicicleta))
        self.assertFalse(milena.puedeUsar(minitramp))

    def test_magneto_baja_dolor_leonardo(self):
        leonardo = self.crearLeonardo()
        magneto = Magneto()

        leonardo.usar(magneto)

        self.assertAlmostEqual(leonardo.nivelDolor, 9)

    def test_magneto_baja_dolor_milena(self):
        milena = self.crearMilena()
        magneto = Magneto()

        milena.usar(magneto)

        self.assertAlmostEqual(milena.nivelDolor, 27)

    def test_bicicleta_en_leonardo(self):
        leonardo = self.crearLeonardo()
        bicicleta = Bicicleta()

        leonardo.usar(bicicleta)

        self.assertAlmostEqual(leonardo.nivelDolor, 6)
        self.assertAlmostEqual(leonardo.fortalezaMuscular, 23)

    def test_minitramp_en_leonardo(self):
        leonardo = self.crearLeonardo()
        minitramp = Minitramp()

        leonardo.usar(minitramp)

        self.assertAlmostEqual(leonardo.fortalezaMuscular, 24)


class TestParte2Rutinas(unittest.TestCase):
    def crearRutinaLeonardo(self):
        bicicleta = Bicicleta()
        minitramp = Minitramp()
        magneto = Magneto()
        return [bicicleta, minitramp, bicicleta, magneto]

    def test_rutina_leonardo(self):
        leonardo = Paciente("Leonardo", 40, 20, 10)
        leonardo.asignarRutina(self.crearRutinaLeonardo())

        self.assertTrue(leonardo.puedeHacerRutina())

        leonardo.hacerSesion()

        self.assertAlmostEqual(leonardo.nivelDolor, 1.8)
        self.assertAlmostEqual(leonardo.fortalezaMuscular, 30)

    def test_milena_no_puede_hacer_rutina(self):
        milena = Paciente("Milena", 2, 50, 30)
        milena.asignarRutina([Magneto(), Bicicleta()])

        self.assertFalse(milena.puedeHacerRutina())


if __name__ == "__main__":
    unittest.main()
