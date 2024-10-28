from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    API_URL: str = "https://example.com"
    DOMAIN: str = "your-default-domain" 
    API_KEY: str = "your-default-api-key"
    CORS_ORIGINS: List[str] = ["*"]
    
    # Add these new fields
    database_url: str = "sqlite:///./sql_app.db"
    vite_api_url: str = "http://localhost:8000"
    
    class Config:
        env_file = ".env"
        # Allow extra fields from environment variables
        extra = "allow"
