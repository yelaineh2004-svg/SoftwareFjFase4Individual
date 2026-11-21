"""Clase abstracta común para los servicios."""
from abc import ABC, abstractmethod
from models.entidad import Entidad
from exceptions.excepciones import DatosInvalidosError, ReservaError

class Servicio(Entidad, ABC):
    """Clase abstracta para todos los servicios ofrecidos por Software FJ."""

    def __init__(self, identificador, nombre, tarifa_base, disponible=True):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")
        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa base debe ser un número positivo.")
        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)
        self._disponible = bool(disponible)

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise DatosInvalidosError("La disponibilidad debe ser True o False.")
        self._disponible = valor

    def validar_parametros(self, duracion):
        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidosError("La duración debe ser un número positivo.")

    def calcular_costo(self, duracion, impuesto=0.19, descuento=0):
        """
        Método con variantes de llamada:
        calcular_costo(duracion)
        calcular_costo(duracion, impuesto)
        calcular_costo(duracion, impuesto, descuento)
        En Python se implementa mediante parámetros opcionales (*sobrecarga simulada*).
        """
        self.validar_parametros(duracion)
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self._tarifa_base * float(duracion)
        total = subtotal * (1 - descuento) * (1 + impuesto)
        if total < 0:
            raise ReservaError("El cálculo produjo un valor negativo.")
        return round(total, 2)

    @abstractmethod
    def describir_servicio(self):
        raise NotImplementedError

    @abstractmethod
    def mostrar_informacion(self):
        raise NotImplementedError