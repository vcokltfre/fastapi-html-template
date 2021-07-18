from os import getenv

from asyncpg import Pool, create_pool


class Database:
    def __init__(self) -> None:
        self.pool: Pool = None

    async def ainit(self) -> None:
        self.pool = await create_pool(
            dsn=getenv("DB_DSN", f"postgres://root:password@localhost:5432/{getenv('DB_DB', 'site')}")
        )
