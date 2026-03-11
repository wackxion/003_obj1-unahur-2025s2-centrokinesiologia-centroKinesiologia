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


