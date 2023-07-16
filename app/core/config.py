import os
import secrets
from typing import Any, Dict, Optional

from pydantic import PostgresDsn, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    BASE_DIR: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

    HOST: str = 'localhost'
    PORT: int = 80

    SECRET_KEY: str = secrets.token_urlsafe(32)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = '5432'
    POSTGRES_DATABASE_URI: Optional[str] = None

    @validator('POSTGRES_DATABASE_URI', pre=True)
    def assemble_db_connection(
        cls,
        v: Optional[str],
        values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return str(PostgresDsn.build(
            scheme='asyncpg',
            username=values.get('POSTGRES_USER'),
            password=values.get('POSTGRES_PASSWORD'),
            host=values.get('POSTGRES_SERVER'),
            path=f'{values.get("POSTGRES_DB") or ""}',
            port=values.get('POSTGRES_PORT')
        ))

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()

TORTOISE_ORM = {
    'connections': {
         'default': settings.POSTGRES_DATABASE_URI
    },
    'apps': {
        'models': {
            'models': ['app.services.database.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}
