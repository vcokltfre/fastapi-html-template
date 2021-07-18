from os import getenv

from aioredis import Redis as _Redis, create_redis_pool


class Redis:
    def __init__(self) -> None:
        self.pool: _Redis = None

    async def ainit(self) -> None:
        self.pool = await create_redis_pool(address=getenv("REDIS_ADDR", "redis://localhost:6379"))
