import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AtmosIQ"
TAGLINE = "Turning Air Quality Data into Everyday Decisions"

AIRNOW_API_KEY = os.getenv("AIRNOW_API_KEY")

if not AIRNOW_API_KEY:
    raise EnvironmentError(
        "AIRNOW_API_KEY is not set. "
        "Copy .env.example to .env and add your AirNow API key."
    )

AIRNOW_CURRENT_OBSERVATION_URL = "https://www.airnowapi.org/aq/observation/zipCode/current/"
AIRNOW_DISTANCE_MILES = 25

# ── Logging configuration ────────────────────────────────────────────────────

_LOG_DIR = Path(__file__).parent / "logs"
_LOG_FILE = _LOG_DIR / "atmosiq.log"
_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def _configure_logging() -> None:
    root_logger = logging.getLogger()

    if root_logger.handlers:
        return

    root_logger.setLevel(logging.INFO)

    _LOG_DIR.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(_LOG_FORMAT, datefmt=_LOG_DATE_FORMAT)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        _LOG_FILE,
        maxBytes=1_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)


_configure_logging()
