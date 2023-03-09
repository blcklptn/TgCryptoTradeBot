from dotenv import load_dotenv
from pydantic import BaseSettings

class Settings(BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: str

    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    BOT_TOKEN: str

settings = Settings()