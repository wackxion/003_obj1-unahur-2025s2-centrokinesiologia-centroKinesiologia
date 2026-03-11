
class Aparato:
    """Clase base para todos los aparatos del centro."""

    def __init__(self, color="blanco"):
        self.color = color

    def puedeSerUsadoPor(self, paciente):
        # Regla por defecto: cualquier paciente puede usar el aparato.
        return True

    def aplicarEfecto(self, paciente):
        # Cada subclase debe definir su propio efecto.
        raise NotImplementedError("Cada subclase debe implementar aplicarEfecto")


class Magneto(Aparato):
    """Disminuye el dolor un 10%."""

    def aplicarEfecto(self, paciente):
        paciente.nivelDolor *= 0.9


class Bicicleta(Aparato):
    """Solo mayores de 8 anos; baja dolor y sube fortaleza."""

    def puedeSerUsadoPor(self, paciente):
        return paciente.edad > 8

    def aplicarEfecto(self, paciente):
        paciente.nivelDolor -= 4
        paciente.fortalezaMuscular += 3


class Minitramp(Aparato):
    """Solo si el dolor es menor a 20; fortalece segun edad."""

    def puedeSerUsadoPor(self, paciente):
        return paciente.nivelDolor < 20

    def aplicarEfecto(self, paciente):
        paciente.fortalezaMuscular += paciente.edad * 0.1




