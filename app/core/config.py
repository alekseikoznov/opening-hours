from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Openning Hours'
    app_description: str = 'Сервис для выбора времени похода в ресторан!'

    class Config:
        env_file = '.env'


settings = Settings()
