from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    API_URL: str = "https://example.com"
    DOMAIN: str = "your-default-domain" 
    API_KEY: str = "your-default-api-key"
    CORS_ORIGINS: List[str] = ["*"]
    
    class Config:
        env_file = ".env"
