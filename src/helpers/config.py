from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    APP_PORT: int
    APP_HOST: str
    APP_URL: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHANK_SIZE: int
    
    MONGODB_URL: str
    MONGODB_DATABASE: str
    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()
