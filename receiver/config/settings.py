from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'tg-bot-service-receiver'

    TG_BOT_TOKEN: str = 'tg-bot-token'
    TG_API_ID: str = 'tg-api-id'
    TG_API_HASH: str = 'tg-api-hash'
    TG_SESSION_NAME: str = 'tg_session_receiver'

    GW_ROOT_URL: str = 'https://some.host'
    GW_API_KEY: str = 'secret-api-key'

    class Config:
        case_sensitive = True


settings = Settings()
