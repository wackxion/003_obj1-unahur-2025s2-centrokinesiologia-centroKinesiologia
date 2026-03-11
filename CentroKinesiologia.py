class CentroKinesiologia:
    def __init__(self):
        self.pacientes = []
        self.aparatos = []

    def agregarPaciente(self, paciente):
        self.pacientes.append(paciente)

    def agregarAparato(self, aparato):
        self.aparatos.append(aparato)

    def coloresAparatosSinRepetidos(self):
        # set evita colores repetidos; se retorna como lista para uso externo.
        return list({aparato.color for aparato in self.aparatos})

    def pacientesMenoresDe8(self):
        return [paciente for paciente in self.pacientes if paciente.edad < 8]

    def cantidadPacientesQueNoPuedenCumplirSesion(self):
        return sum(1 for paciente in self.pacientes if not paciente.puedeHacerRutina())

    def estaEnOptimasCondiciones(self):
        return all(not aparato.necesitaMantenimiento() for aparato in self.aparatos)

    def estaComplicado(self):
        if not self.aparatos:
            return False
        aparatosConMantenimiento = sum(1 for aparato in self.aparatos if aparato.necesitaMantenimiento())
        return aparatosConMantenimiento >= (len(self.aparatos) / 2)

    def registrarVisitaTecnico(self):
        for aparato in self.aparatos:
            if aparato.necesitaMantenimiento():
                aparato.realizarMantenimiento()