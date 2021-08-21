from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST = "0.0.0.0"
    PORT = 4000
    WORKERS = 1
    RELOAD = True

    POSTGRES_DSN = "postgresql://anl:example@localhost:5432/anl"


settings = Settings()
