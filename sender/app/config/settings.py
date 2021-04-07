import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'

    PROJECT_NAME: str = 'tg-bot-service-sender'

    TG_BOT_TOKEN: str = '1288582515:AAEb1B467GH7_J6gziV3c97p7wN8AZhx6PI'
    TG_API_ID: str = '3472915'
    TG_API_HASH: str = '5b01fa0d397c04a794a04e2cb04d4141'
    TG_SESSION_NAME: str = 'tg_session_sender'

    TG_FILES_CHAT_ID: int = 787626773

    class Config:
        case_sensitive = True


settings = Settings()
