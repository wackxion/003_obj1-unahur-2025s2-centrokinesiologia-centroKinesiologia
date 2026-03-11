import unittest

from aparatos import Bicicleta, Magneto, Minitramp
from CentroKinesiologia import CentroKinesiologia
from pacientes import Caprichoso, Paciente, RapidaRecuperacion, Resistente


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
        milena = Paciente("Milena", 3, 50, 30)
        milena.asignarRutina([Magneto(), Bicicleta()])

        self.assertFalse(milena.puedeHacerRutina())


class TestParte3TiposDePacientes(unittest.TestCase):
    def crearRutinaLeonardo(self):
        bicicleta = Bicicleta()
        minitramp = Minitramp()
        magneto = Magneto()
        return [bicicleta, minitramp, bicicleta, magneto]

    def test_nicolas_resistente(self):
        nicolas = Resistente("Nicolas", 40, 20, 10)
        nicolas.asignarRutina(self.crearRutinaLeonardo())

        self.assertTrue(nicolas.puedeHacerRutina())

        nicolas.hacerSesion()

        self.assertAlmostEqual(nicolas.nivelDolor, 1.8)
        self.assertAlmostEqual(nicolas.fortalezaMuscular, 34)

    def test_victoria_caprichosa_no_puede(self):
        victoria = Caprichoso("Victoria", 30, 40, 10)
        victoria.asignarRutina(self.crearRutinaLeonardo())

        self.assertFalse(victoria.puedeHacerRutina())

    def test_julian_caprichoso_hace_rutina_dos_veces(self):
        bicicletaRoja = Bicicleta(color="rojo")
        magnetoVerde = Magneto(color="verde")
        bicicletaBlanca = Bicicleta(color="blanco")

        julian = Caprichoso("Julian", 20, 50, 54)
        julian.asignarRutina([bicicletaRoja, magnetoVerde, bicicletaBlanca])

        self.assertTrue(julian.puedeHacerRutina())

        julian.hacerSesion()

        self.assertAlmostEqual(julian.nivelDolor, 29.3)
        self.assertAlmostEqual(julian.fortalezaMuscular, 62)

    def test_zoe_rapida_recuperacion_con_decremento_configurable(self):
        zoe = RapidaRecuperacion("Zoe", 50, 40, 14)
        zoe.asignarRutina(self.crearRutinaLeonardo())

        self.assertTrue(zoe.puedeHacerRutina())

        valorAnterior = RapidaRecuperacion.decrementoDolor
        RapidaRecuperacion.configurarDecrementoDolor(2)
        try:
            zoe.hacerSesion()
        finally:
            RapidaRecuperacion.configurarDecrementoDolor(valorAnterior)

        self.assertAlmostEqual(zoe.nivelDolor, 3.4)
        self.assertAlmostEqual(zoe.fortalezaMuscular, 51)


class TestParte4Centro(unittest.TestCase):
    def test_colores_aparatos_sin_repetidos(self):
        centro = CentroKinesiologia()
        centro.agregarAparato(Magneto(color="blanco"))
        centro.agregarAparato(Bicicleta(color="rojo"))
        centro.agregarAparato(Minitramp(color="blanco"))

        colores = centro.coloresAparatosSinRepetidos()

        self.assertEqual(set(colores), {"blanco", "rojo"})

    def test_pacientes_menores_de_8(self):
        centro = CentroKinesiologia()
        milena = Paciente("Milena", 3, 50, 30)
        leonardo = Paciente("Leonardo", 40, 20, 10)
        centro.agregarPaciente(milena)
        centro.agregarPaciente(leonardo)

        menores = centro.pacientesMenoresDe8()

        self.assertEqual([p.nombre for p in menores], ["Milena"])

    def test_cantidad_pacientes_que_no_pueden_cumplir_sesion(self):
        centro = CentroKinesiologia()
        leonardo = Paciente("Leonardo", 40, 20, 10)
        leonardo.asignarRutina([Bicicleta(), Minitramp(), Bicicleta(), Magneto()])
        milena = Paciente("Milena", 3, 50, 30)
        milena.asignarRutina([Magneto(), Bicicleta()])
        centro.agregarPaciente(leonardo)
        centro.agregarPaciente(milena)

        self.assertEqual(centro.cantidadPacientesQueNoPuedenCumplirSesion(), 1)


class TestParte5Mantenimiento(unittest.TestCase):
    def test_magneto_necesita_mantenimiento_y_se_repara(self):
        magneto = Magneto()
        paciente = Paciente("Prueba", 30, 10, 10)

        # 701 usos dejan imantacion en 99 (800 - 701) y debe pedir mantenimiento.
        for _ in range(701):
            paciente.usar(magneto)

        self.assertTrue(magneto.necesitaMantenimiento())

        magneto.realizarMantenimiento()

        self.assertEqual(magneto.imantacion, 599)
        self.assertFalse(magneto.necesitaMantenimiento())

    def test_bicicleta_contadores_y_mantenimiento(self):
        bicicleta = Bicicleta()
        paciente = Paciente("Adulto", 40, 10, 60)

        # Cada uso con dolor > 30 suma tornillos y, por edad 30..50, tambien aceite.
        for _ in range(5):
            paciente.nivelDolor = 60
            paciente.usar(bicicleta)

        self.assertEqual(bicicleta.desajustesTornillos, 5)
        self.assertEqual(bicicleta.perdidasAceite, 5)
        self.assertTrue(bicicleta.necesitaMantenimiento())

        bicicleta.realizarMantenimiento()

        self.assertEqual(bicicleta.desajustesTornillos, 0)
        self.assertEqual(bicicleta.perdidasAceite, 0)
        self.assertFalse(bicicleta.necesitaMantenimiento())

    def test_minitramp_nunca_necesita_mantenimiento(self):
        minitramp = Minitramp()
        paciente = Paciente("Leonardo", 40, 20, 10)

        paciente.usar(minitramp)

        self.assertFalse(minitramp.necesitaMantenimiento())
        minitramp.realizarMantenimiento()
        self.assertFalse(minitramp.necesitaMantenimiento())

    def test_estado_centro_y_visita_tecnico(self):
        centro = CentroKinesiologia()
        magneto = Magneto()
        bicicleta = Bicicleta()
        minitramp = Minitramp()
        paciente = Paciente("Adulto", 40, 10, 60)

        # Deja a magneto y bicicleta en estado de mantenimiento.
        for _ in range(701):
            paciente.nivelDolor = 60
            paciente.usar(magneto)
        for _ in range(5):
            paciente.nivelDolor = 60
            paciente.usar(bicicleta)

        centro.agregarAparato(magneto)
        centro.agregarAparato(bicicleta)
        centro.agregarAparato(minitramp)

        self.assertFalse(centro.estaEnOptimasCondiciones())
        self.assertTrue(centro.estaComplicado())

        centro.registrarVisitaTecnico()

        self.assertTrue(centro.estaEnOptimasCondiciones())
        self.assertFalse(centro.estaComplicado())


if __name__ == "__main__":
    unittest.main()
