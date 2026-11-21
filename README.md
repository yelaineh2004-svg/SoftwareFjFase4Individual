# software-fj-fase4-individual
Proyecto colaborativo – Sistema Integral de Gestión de Clientes, Servicios y Reservas – Programación 213023_6.

## Descripción
Sistema de consola en Python para administrar clientes, servicios y reservas mediante POO. No utiliza bases de datos: la información de negocio se conserva en listas durante la ejecución. Los eventos y errores se registran en `logs/software-fj-fase4-individual.log`.

## Estructura del proyecto
```text
software-fj-fase4-individual/
├── main.py
├── models/
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   └── reserva.py
├── services/
│   ├── reserva_salas.py
│   ├── alquiler_equipos.py
│   └── asesoria.py
├── exceptions/
│   └── excepciones.py
├── utils/
│   └── logger.py
├── logs/
│   └── .gitkeep
└── README.md
```

## Ejecución
Desde la carpeta raíz `software-fj-fase4-individual`, ejecutar `python main.py` (Windows: `py main.py`). No requiere instalar librerías externas.

## POO implementada
- Abstracción: `Entidad` y `Servicio`.
- Herencia: Cliente y los servicios especializados derivan de clases base.
- Encapsulación: atributos internos y propiedades validadas.
- Polimorfismo: los servicios sobrescriben métodos descriptivos y de cálculo.
- Sobrecarga simulada: Python no admite sobrecarga tradicional por firma; se emplean parámetros opcionales y argumentos específicos en `calcular_costo()`.

## Excepciones y logs
Incluye excepciones personalizadas, bloques `try/except`, `try/except/else`, `try/except/finally` y encadenamiento mediante `raise ... from error`. El archivo `logs/software-fj-fase4-individual.log` se crea automáticamente al ejecutar el sistema.

## Pruebas
`main.py` ejecuta 18 escenarios válidos e inválidos para demostrar registros, servicios, reservas, disponibilidad, validaciones y cálculos.

## Nota sobre el trabajo individual
La estructura y los módulos pueden ser desarrollados por una sola persona si el docente autoriza esa modalidad. Los commits de GitHub deben reflejar únicamente aportes reales.
