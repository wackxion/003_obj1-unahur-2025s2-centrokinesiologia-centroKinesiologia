class Paciente:
    """Modelo base de paciente con su rutina de aparatos."""

    def __init__(self, nombre, edad, fortalezaMuscular, nivelDolor, rutina=None):
        self.nombre = nombre
        self.edad = edad
        self.fortalezaMuscular = fortalezaMuscular
        self.nivelDolor = nivelDolor
        # Si no llega rutina, se inicializa vacia.
        self.rutina = rutina or []

    def puedeUsar(self, aparato):
        return aparato.puedeSerUsadoPor(self)

    def usar(self, aparato):
        # Primero se valida; despues se aplica el efecto del aparato.
        if not self.puedeUsar(aparato):
            raise ValueError(f"{self.nombre} no puede usar {aparato.__class__.__name__}")
        aparato.aplicarEfecto(self)

    def asignarRutina(self, rutina):
        self.rutina = rutina

    def puedeHacerRutina(self):
        # Solo puede iniciar si puede usar todos los aparatos al comienzo.
        return all(self.puedeUsar(aparato) for aparato in self.rutina)

    def hacerSesion(self):
        # Ejecuta la rutina completa en el orden definido.
        if not self.puedeHacerRutina():
            raise ValueError(f"{self.nombre} no puede hacer su rutina completa")
        for aparato in self.rutina:
            self.usar(aparato)

class Resistente(Paciente):
    """Suma 1 punto de fortaleza por cada aparato usado en su sesion."""

    def hacerSesion(self):
        super().hacerSesion()
        # Si repite aparatos, tambien cuentan para este adicional.
        self.fortalezaMuscular += len(self.rutina)

class Caprichoso(Paciente):
    """Puede hacer rutina solo si hay al menos un aparato rojo y la ejecuta dos veces."""

    def puedeHacerRutina(self):
        hayAparatoRojo = any(aparato.color == "rojo" for aparato in self.rutina)
        return super().puedeHacerRutina() and hayAparatoRojo

    def hacerSesion(self):
        if not self.puedeHacerRutina():
            raise ValueError(f"{self.nombre} no puede hacer su rutina completa")
        # Hace dos veces la rutina asignada en cada sesion.
        for _ in range(2):
            for aparato in self.rutina:
                self.usar(aparato)


class RapidaRecuperacion(Paciente):
    """Luego de la rutina, baja dolor en un valor compartido por todos."""

    decrementoDolor = 3

    @classmethod
    def configurarDecrementoDolor(cls, nuevoValor):
        # Se guarda a nivel clase para que aplique a todos los pacientes de este tipo.
        cls.decrementoDolor = nuevoValor

    def hacerSesion(self):
        super().hacerSesion()
        self.nivelDolor -= type(self).decrementoDolor