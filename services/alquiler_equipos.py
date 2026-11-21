"""Servicio especializado de alquiler de equipos."""
from models.servicio import Servicio
from exceptions.excepciones import DatosInvalidosError

class AlquilerEquipo(Servicio):
    """Servicio especializado de alquiler de equipos."""

    def __init__(self, identificador, nombre, tarifa_base, unidades, disponible=True):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        if isinstance(unidades, bool) or not isinstance(unidades, int) or unidades <= 0:
            raise DatosInvalidosError("Las unidades deben ser un entero positivo.")
        self.unidades = unidades

    def calcular_costo(self, duracion, impuesto=0.19, descuento=0, cantidad=1):
        self.validar_parametros(duracion)
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad <= 0:
            raise DatosInvalidosError("La cantidad debe ser un entero positivo.")
        if cantidad > self.unidades:
            raise DatosInvalidosError(f"Solo hay {self.unidades} unidades disponibles.")
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self._tarifa_base * float(duracion) * cantidad
        return round(subtotal * (1 - descuento) * (1 + impuesto), 2)

    def describir_servicio(self):
        return f"Alquiler de {self.nombre}; unidades disponibles: {self.unidades}."

    def mostrar_informacion(self):
        return f"{self.identificador} | {self.describir_servicio()} | Tarifa: ${self._tarifa_base:.2f}"
