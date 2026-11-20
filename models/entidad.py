"""Clase abstracta base de las entidades."""
from abc import ABC, abstractmethod
from exceptions.excepciones import ParametroFaltanteError

class Entidad(ABC):
    """Clase abstracta que representa una entidad identificable del sistema."""

    def __init__(self, identificador):
        if identificador is None or not str(identificador).strip():
            raise ParametroFaltanteError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Expone el identificador sin permitir modificarlo directamente."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Obliga a las entidades concretas a describir su información."""
        raise NotImplementedError
