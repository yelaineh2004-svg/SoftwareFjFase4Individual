"""Configuración del registro de eventos y errores."""
import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.INFO)
if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    handler = logging.FileHandler(LOG_DIR / "software_fj.log", encoding="utf-8")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
