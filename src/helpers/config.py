from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    APP_PORT: int
    APP_HOST: str
    APP_URL: str
    OPENAI_API_KEY: str
    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()
