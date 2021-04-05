import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api_v1'
    SECRET_KEY: str = secrets.token_urlsafe(32)
    X_API_TOKEN: str = 'no-secret-yet'

    PROJECT_NAME: str = 'tg-bot-service'

    class Config:
        case_sensitive = True


settings = Settings()
