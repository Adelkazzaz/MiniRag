from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int
    # <==================-Database-Connection-=================>
    MONGODB_URL: str
    MONGODB_DATABASE: str
    # <====================== llm config ===========================>
    GENERATION_PROVIDER: str
    EMBEDDING_PROVIDER: str
    
    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DAFAULT_MAX_CHARACTERS: int = None
    GENERATION_DAFAULT_MAX_TOKENS: int = None
    GENERATION_DAFAULT_TEMPERATURE: float = None
    # <=================================================>
    # <====================== llm openai config ===========================>
    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None
    # <=================================================>
    # <====================== llm cohere config ===========================>
    COHERE_API_KEY: str = None
    
    class Config:
        env_file = ".env"
        
def get_settings():
    return Settings()
