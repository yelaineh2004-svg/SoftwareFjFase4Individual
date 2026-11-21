"""Servicio especializado de reserva de salas."""
from models.servicio import Servicio
from exceptions.excepciones import DatosInvalidosError

class ReservaSala(Servicio):
    """Servicio especializado de reserva de salas."""

    def __init__(self, identificador, nombre, tarifa_base, capacidad, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if isinstance(capacidad, bool) or not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")
        self.capacidad = capacidad

    def validar_parametros(self, duracion, asistentes=1):
        super().validar_parametros(duracion)
        if isinstance(asistentes, bool) or not isinstance(asistentes, int) or asistentes <= 0:
            raise DatosInvalidosError("El número de asistentes debe ser un entero positivo.")
        if asistentes > self.capacidad:
            raise DatosInvalidosError(
                f"La sala admite máximo {self.capacidad} asistentes; se solicitaron {asistentes}."
            )

    def calcular_costo(self, duracion, impuesto=0.19, descuento=0, asistentes=1):
        self.validar_parametros(duracion, asistentes)
        return super().calcular_costo(duracion, impuesto, descuento)

    def describir_servicio(self):
        return f"Sala '{self.nombre}' con capacidad para {self.capacidad} personas."

    def mostrar_informacion(self):
        return f"{self.identificador} | {self.describir_servicio()} | Tarifa/hora: ${self._tarifa_base:.2f}"
