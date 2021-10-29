tortoise_config = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": "",
                "host": "",
                "password": "",
                "port": "",
                "user": "",
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