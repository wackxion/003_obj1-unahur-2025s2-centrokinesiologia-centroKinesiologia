
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

    def necesitaMantenimiento(self):
        # Por defecto no necesita mantenimiento; cada subclase redefine si aplica.
        return False

    def realizarMantenimiento(self):
        # Accion vacia para aparatos sin mantenimiento.
        return None


class Magneto(Aparato):
    """Disminuye el dolor un 10%."""

    def __init__(self, color="blanco"):
        super().__init__(color)
        # Estado inicial segun enunciado.
        self.imantacion = 800

    def aplicarEfecto(self, paciente):
        # Efecto sobre paciente.
        paciente.nivelDolor *= 0.9
        # Efecto sobre aparato: pierde imantacion por uso.
        self.imantacion -= 1

    def necesitaMantenimiento(self):
        return self.imantacion < 100

    def realizarMantenimiento(self):
        self.imantacion += 500


class Bicicleta(Aparato):
    """Solo mayores de 8 anos; baja dolor y sube fortaleza."""

    def __init__(self, color="blanco"):
        super().__init__(color)
        # Contadores desde ultimo mantenimiento.
        self.desajustesTornillos = 0
        self.perdidasAceite = 0

    def puedeSerUsadoPor(self, paciente):
        return paciente.edad > 8

    def aplicarEfecto(self, paciente):
        # El estado mecanico depende de las condiciones antes del uso.
        dolorAntes = paciente.nivelDolor
        paciente.nivelDolor -= 4
        paciente.fortalezaMuscular += 3

        if dolorAntes > 30:
            self.desajustesTornillos += 1
            if 30 <= paciente.edad <= 50:
                self.perdidasAceite += 1

    def necesitaMantenimiento(self):
        return self.desajustesTornillos >= 10 or self.perdidasAceite >= 5

    def realizarMantenimiento(self):
        self.desajustesTornillos = 0
        self.perdidasAceite = 0


class Minitramp(Aparato):
    """Solo si el dolor es menor a 20; fortalece segun edad."""

    def puedeSerUsadoPor(self, paciente):
        return paciente.nivelDolor < 20

    def aplicarEfecto(self, paciente):
        paciente.fortalezaMuscular += paciente.edad * 0.1

    def necesitaMantenimiento(self):
        return False

    def realizarMantenimiento(self):
        return None




