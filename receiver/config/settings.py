from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'tg-bot-service-receiver'

    TG_BOT_TOKEN: str = 'your-bot-token'
    TG_API_ID: str = 'your-bot-api-id'
    TG_API_HASH: str = 'your-bot-api-hash'
    TG_SESSION_NAME: str = 'tg_session'

    class Config:
        case_sensitive = True


settings = Settings()
