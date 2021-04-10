import os
import logging
from logging.handlers import RotatingFileHandler

from config import settings


def gateway_api_driver_logger_init() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    if not os.path.exists(settings.LOGS_DIR):
        os.makedirs(settings.LOGS_DIR)

    rfh = RotatingFileHandler(
        filename=f'{settings.LOGS_DIR}{settings.GatewayAPIDriverLogger.FILENAME}',
        maxBytes=settings.GatewayAPIDriverLogger.MAX_BYTES,
        backupCount=settings.GatewayAPIDriverLogger.BACKUP_COUNT,
    )
    rfh.setFormatter(settings.GatewayAPIDriverLogger.FORMATTER)
    logger.addHandler(rfh)
    return logger
