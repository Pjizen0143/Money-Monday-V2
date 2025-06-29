from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_BETA_STR: str = "/api/beta"
    SECRET_KEY: str = "KEY"
    # 60 minutes * 24 hours * 1 day = 1 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1