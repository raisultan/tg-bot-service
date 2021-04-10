import logging

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'tg-bot-service-receiver'

    TG_BOT_TOKEN: str = 'tg-bot-token'
    TG_API_ID: str = 'tg-api-id'
    TG_API_HASH: str = 'tg-api-hash'
    TG_SESSION_NAME: str = 'tg_session_receiver'

    GW_ROOT_URL: str = 'https://some.host'
    GW_API_KEY: str = 'secret-api-key'

    LOGS_DIR: str = 'logs/'

    class GatewayAPIDriverLogger:
        FILENAME: str = 'gateway_api_driver.log'
        MAX_BYTES: int = 5 * (1024 * 1024)
        BACKUP_COUNT: int = 10
        FORMATTER: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    class Config:
        case_sensitive = True


settings = Settings()
