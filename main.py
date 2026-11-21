"""Punto de entrada y pruebas de integración del sistema software-fj-fase4-individual."""
from models.cliente import Cliente
from models.reserva import Reserva
from models.servicio import Servicio
from services.reserva_salas import ReservaSala
from services.alquiler_equipos import AlquilerEquipo
from services.asesoria import Asesoria
from exceptions.excepciones import DatosInvalidosError
from utils.logger import logger

from models.cliente import Cliente
from models.servicio import Servicio
from models.reserva import Reserva
from exceptions.excepciones import DatosInvalidosError
from utils.logger import logger

class Gestorsoftware-fj-fase4-individual:
    """Administra clientes, servicios y reservas en memoria."""

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError("Solo se pueden registrar objetos Cliente.")
        if any(c.identificador == cliente.identificador for c in self.clientes):
            raise DatosInvalidosError("Ya existe un cliente con ese identificador.")
        self.clientes.append(cliente)
        logger.info("Cliente registrado: %s.", cliente.identificador)
        return cliente

    def registrar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError("Solo se pueden registrar objetos Servicio.")
        if any(s.identificador == servicio.identificador for s in self.servicios):
            raise DatosInvalidosError("Ya existe un servicio con ese identificador.")
        self.servicios.append(servicio)
        logger.info("Servicio registrado: %s.", servicio.identificador)
        return servicio

    def crear_reserva(self, reserva):
        if not isinstance(reserva, Reserva):
            raise DatosInvalidosError("Solo se pueden registrar objetos Reserva.")
        if any(r.identificador == reserva.identificador for r in self.reservas):
            raise DatosInvalidosError("Ya existe una reserva con ese identificador.")
        self.reservas.append(reserva)
        logger.info("Reserva agregada al gestor: %s.", reserva.identificador)
        return reserva

    def listar_clientes(self):
        return [cliente.mostrar_informacion() for cliente in self.clientes]

    def listar_servicios(self):
        # Polimorfismo: cada servicio responde con su propia implementación.
        return [servicio.mostrar_informacion() for servicio in self.servicios]

    def listar_reservas(self):
        return [reserva.mostrar_informacion() for reserva in self.reservas]

def ejecutar_operacion(numero, descripcion, funcion):
    """Ejecuta una operación aislada para que un error no detenga el programa."""
    print(f"\n[{numero}] {descripcion}")
    try:
        resultado = funcion()
    except Exception as error:
        logger.exception("Operación %s fallida: %s", numero, descripcion)
        print(f"ERROR CONTROLADO: {type(error).__name__}: {error}")
    else:
        print("Resultado:", resultado if resultado is not None else "Operación realizada.")
    finally:
        print(f"Fin de la operación {numero}.")


def main():
    sistema = Gestorsoftware-fj-fase4-individual()

    # Objetos iniciales para las demostraciones.
    cliente1 = Cliente("C001", "Laura Pérez", "laura@email.com", "3001234567")
    cliente2 = Cliente("C002", "Carlos Díaz", "carlos@email.com", "3107654321")
    sala = ReservaSala("S001", "Sala Ejecutiva", 50000, 12)
    equipo = AlquilerEquipo("E001", "Proyector HD", 25000, 4)
    asesoria = Asesoria("A001", "Consultoría TI", 80000, "redes y ciberseguridad")

    # 1. Registro correcto de cliente.
    ejecutar_operacion(1, "Registrar cliente válido", lambda: sistema.registrar_cliente(cliente1).mostrar_informacion())

    # 2. Registro correcto de segundo cliente.
    ejecutar_operacion(2, "Registrar segundo cliente", lambda: sistema.registrar_cliente(cliente2).mostrar_informacion())

    # 3. Registro inválido: correo incorrecto.
    ejecutar_operacion(3, "Intentar crear cliente con correo inválido",
        lambda: Cliente("C003", "Ana López", "correo-invalido", "3001234567"))

    # 4. Registro inválido: teléfono con letras.
    ejecutar_operacion(4, "Intentar crear cliente con teléfono inválido",
        lambda: Cliente("C004", "Pedro Ruiz", "pedro@email.com", "abc123"))

    # 5. Registrar servicio de sala.
    ejecutar_operacion(5, "Registrar servicio de salas",
        lambda: sistema.registrar_servicio(sala).mostrar_informacion())

    # 6. Registrar servicio de alquiler de equipos.
    ejecutar_operacion(6, "Registrar servicio de equipos",
        lambda: sistema.registrar_servicio(equipo).mostrar_informacion())

    # 7. Registrar servicio de asesoría.
    ejecutar_operacion(7, "Registrar servicio de asesorías",
        lambda: sistema.registrar_servicio(asesoria).mostrar_informacion())

    # 8. Intentar crear servicio con tarifa negativa.
    ejecutar_operacion(8, "Intentar crear servicio con tarifa negativa",
        lambda: ReservaSala("S002", "Sala inválida", -1000, 10))

    # 9. Crear una reserva correcta.
    reserva1 = None
    def crear_reserva_correcta():
        nonlocal reserva1
        reserva1 = Reserva("R001", cliente1, sala, 2, asistentes=6, descuento=0.10)
        sistema.crear_reserva(reserva1)
        return reserva1.mostrar_informacion()
    ejecutar_operacion(9, "Crear reserva de sala", crear_reserva_correcta)

    # 10. Confirmar reserva.
    ejecutar_operacion(10, "Confirmar reserva R001", lambda: reserva1.confirmar())

    # 11. Procesar reserva y calcular costo con impuesto y descuento.
    ejecutar_operacion(11, "Procesar reserva R001", lambda: f"Total: ${reserva1.procesar():,.2f}")

    # 12. Intentar cancelar una reserva ya procesada.
    ejecutar_operacion(12, "Intentar cancelar reserva procesada", lambda: reserva1.cancelar())

    # 13. Intentar reservar un servicio no disponible.
    equipo.disponible = False
    ejecutar_operacion(13, "Intentar reservar equipo no disponible",
        lambda: Reserva("R002", cliente2, equipo, 3, cantidad=1))

    # 14. Intentar crear reserva con duración negativa.
    ejecutar_operacion(14, "Intentar reservar con duración inválida",
        lambda: Reserva("R003", cliente2, sala, -2, asistentes=2))

    # 15. Intentar procesar reserva sin confirmarla.
    reserva2 = Reserva("R004", cliente2, asesoria, 1.5)
    sistema.crear_reserva(reserva2)
    ejecutar_operacion(15, "Procesar reserva pendiente sin confirmar", lambda: reserva2.procesar())

    # 16. Demostrar método de costo con diferentes variantes de parámetros.
    ejecutar_operacion(16, "Calcular costo solo con duración",
        lambda: f"${asesoria.calcular_costo(2):,.2f}")
    ejecutar_operacion(17, "Calcular costo con impuesto y descuento",
        lambda: f"${asesoria.calcular_costo(2, 0.19, 0.15):,.2f}")

    # 18. Demostrar excepción encadenada provocada por un cálculo inválido.
    reserva3 = Reserva("R005", cliente1, asesoria, 1, impuesto=1.5)
    sistema.crear_reserva(reserva3)
    reserva3.confirmar()
    ejecutar_operacion(18, "Procesar reserva con impuesto inválido (excepción encadenada)",
        lambda: reserva3.procesar())

    # Resumen final: el programa llega aquí aunque existan errores controlados.
    print("\n" + "=" * 65)
    print("RESUMEN FINAL DEL SISTEMA SOFTWARE FJ")
    print("=" * 65)
    print(f"Clientes registrados: {len(sistema.clientes)}")
    print(f"Servicios registrados: {len(sistema.servicios)}")
    print(f"Reservas registradas: {len(sistema.reservas)}")

    print("\nCLIENTES")
    for elemento in sistema.listar_clientes():
        print("-", elemento)

    print("\nSERVICIOS")
    for elemento in sistema.listar_servicios():
        print("-", elemento)

    print("\nRESERVAS")
    for elemento in sistema.listar_reservas():
        print("-", elemento)

    print("\nEl sistema finalizó correctamente. Consulte logs/software-fj-fase4-individual.log.")


if __name__ == "__main__":
    main()
