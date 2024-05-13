from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Cursor Payment Microservice"
    admin_email: str
    database_url: str = "postgresql+asyncpg://zwjycwty:RSuVL1oZVi7RlRaa5yIamrW5yn9N5stL@abul.db.elephantsql.com/zwjycwty"
    secret_key: str
    stripe_secret_key: str

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
