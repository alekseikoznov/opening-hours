from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Openning Hours'
    app_description: str = 'Service for rendering in human readable format'

    class Config:
        env_file = '.env'


settings = Settings()
