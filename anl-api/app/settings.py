from pydantic import BaseSettings


class Settings(BaseSettings):
    HOST = "0.0.0.0"
    PORT = 4000
    WORKERS = 1
    RELOAD = True

    POSTGRES_DSN = "postgresql://anl:example@localhost:5432/anl"
    POSTGRES_ECHO = True

    SCORE_ERROR_THRESHOLD = 0.5


settings = Settings()
