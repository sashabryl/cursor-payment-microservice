from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Curson Payment Microservice"
    admin_email: str
    database_url: str = "postgresql+asyncpg://user:password@localhost/dbname"
    secret_key: str

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
