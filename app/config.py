import os

class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "pass")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "url_shortener")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "db")
    POSTGRES_PORT: int = 5432

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    BASE_URL: str = os.getenv("BASE_URL", "http://localhost:8000")

settings = Settings()
