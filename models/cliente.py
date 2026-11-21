"""Modelo Cliente con encapsulación y validaciones."""
from models.entidad import Entidad
from exceptions.excepciones import DatosInvalidosError

class Cliente(Entidad):
    """Cliente con datos encapsulados y validados."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise DatosInvalidosError("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        numero = str(valor).replace(" ", "").replace("-", "")
        if not numero.isdigit() or not 7 <= len(numero) <= 15:
            raise DatosInvalidosError("El teléfono debe contener entre 7 y 15 dígitos.")
        self._telefono = numero

    def mostrar_informacion(self):
        return f"Cliente {self.identificador}: {self.nombre} | {self.correo} | {self.telefono}"