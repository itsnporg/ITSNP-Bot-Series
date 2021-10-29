import os
from dotenv import load_dotenv

load_dotenv()

tortoise_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": os.environ.get("DATABASE_NAME"),
                "host": os.environ.get("DATABASE_HOST"),
                "password": os.environ.get("DATABASE_PASSWORD"),
                "port": os.environ.get("DATABASE_PORT"),
                "user": os.environ.get("DATABASE_USER"),
            },
        }
    },
    "apps": {
        "main": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
}
