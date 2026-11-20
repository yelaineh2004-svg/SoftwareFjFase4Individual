"""Modelo Reserva: estados, confirmación, cancelación y procesamiento."""
from datetime import datetime
from models.entidad import Entidad
from models.cliente import Cliente
from models.servicio import Servicio
from exceptions.excepciones import (DatosInvalidosError, OperacionNoPermitidaError,
    ServicioNoDisponibleError, ReservaError)
from utils.logger import logger

class Reserva(Entidad):
    """Reserva que relaciona un cliente, un servicio, duración y estado."""

    ESTADOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA", "PROCESADA")

    def __init__(self, identificador, cliente, servicio, duracion, **opciones):
        super().__init__(identificador)
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("La reserva requiere un objeto Cliente válido.")
        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("La reserva requiere un objeto Servicio válido.")
        servicio.validar_parametros(duracion)
        if not servicio.disponible:
            raise ServicioNoDisponibleError(f"El servicio {servicio.nombre} no está disponible.")
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = float(duracion)
        self._opciones = opciones
        self._estado = "PENDIENTE"
        self._costo = None
        self._creada = datetime.now()
        logger.info("Reserva %s creada para cliente %s.", self.identificador, cliente.identificador)

    @property
    def estado(self):
        return self._estado

    @property
    def costo(self):
        return self._costo

    def confirmar(self):
        if self._estado != "PENDIENTE":
            raise OperacionNoPermitidaError("Solo se puede confirmar una reserva pendiente.")
        if not self._servicio.disponible:
            raise ServicioNoDisponibleError("El servicio dejó de estar disponible.")
        self._estado = "CONFIRMADA"
        logger.info("Reserva %s confirmada.", self.identificador)

    def cancelar(self):
        if self._estado in ("CANCELADA", "PROCESADA"):
            raise OperacionNoPermitidaError("No se puede cancelar una reserva cancelada o procesada.")
        self._estado = "CANCELADA"
        logger.info("Reserva %s cancelada.", self.identificador)

    def procesar(self):
        if self._estado != "CONFIRMADA":
            raise OperacionNoPermitidaError("La reserva debe estar confirmada antes de procesarse.")
        try:
            self._costo = self._servicio.calcular_costo(
                self._duracion, **self._opciones
            )
        except Exception as error:
            # Encadenamiento: el error de cálculo queda como causa de ReservaError.
            raise ReservaError("No fue posible calcular el costo de la reserva.") from error
        else:
            self._estado = "PROCESADA"
            logger.info("Reserva %s procesada. Total: $%.2f", self.identificador, self._costo)
            return self._costo
        finally:
            logger.info("Finalizó el intento de procesamiento de la reserva %s.", self.identificador)

    def mostrar_informacion(self):
        costo = f"${self._costo:.2f}" if self._costo is not None else "Pendiente"
        return (
            f"Reserva {self.identificador} | Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | Duración: {self._duracion} | "
            f"Estado: {self._estado} | Costo: {costo}"
        )
