from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql_asyncpg://api-dio@localhost/api-dio')
    
settings = Settings()