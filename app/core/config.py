from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Openning Hours'
    app_description: str = 'Сервис для выбора времени похода в ресторан!'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
