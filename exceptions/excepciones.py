"""Excepciones personalizadas del sistema SoftwareFjFase4Individual."""
class ErrorSistema(Exception):
    """Clase base para errores controlados."""
class DatosInvalidosError(ErrorSistema):
    """Dato que no cumple las reglas de validación."""
class ParametroFaltanteError(ErrorSistema):
    """Falta un parámetro obligatorio."""
class OperacionNoPermitidaError(ErrorSistema):
    """Operación incompatible con el estado actual."""
class ServicioNoDisponibleError(ErrorSistema):
    """Servicio no disponible para reservar."""
class ReservaError(ErrorSistema):
    """Error durante el procesamiento de una reserva."""
