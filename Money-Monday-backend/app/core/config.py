from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_BETA_STR: str = "/api/beta"
    SECRET_KEY: str = "KEY"
    ALGORITHM: str = "HS256"
    # 60 minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60


settings = Settings()