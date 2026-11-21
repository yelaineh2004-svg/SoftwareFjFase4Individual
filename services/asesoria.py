"""Servicio especializado de asesorías."""
from models.servicio import Servicio
from exceptions.excepciones import DatosInvalidosError

class Asesoria(Servicio):
    """Servicio especializado de asesoría por horas."""

    def __init__(self, identificador, nombre, tarifa_base, especialidad, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("La especialidad de la asesoría es obligatoria.")
        self.especialidad = especialidad.strip()

    def describir_servicio(self):
        return f"Asesoría especializada en {self.especialidad}."

    def mostrar_informacion(self):
        return f"{self.identificador} | {self.describir_servicio()} | Tarifa/hora: ${self._tarifa_base:.2f}"
