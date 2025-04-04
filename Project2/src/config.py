from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str  # Automatically loads from the .env file

model_config = SettingsConfigDict(
    env_file=".env",  # Relative path to the .env file
    extra="ignore"
)

Config = Settings(DATABASE_URL="postgresql+asyncpg://postgres:Jangotravinay@localhost:5432/python")  # Default value if .env is not found
