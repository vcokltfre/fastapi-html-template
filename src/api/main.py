from typing import Coroutine

from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles

load_dotenv()

from .routing import router
from .utils import Database, Redis


app = FastAPI(docs_url=None)
app.mount("/static", StaticFiles(directory="src/web/static"), "static")
app.include_router(router)

db = Database()
redis = Redis()

@app.on_event("startup")
async def on_startup() -> None:
    """Initialize the database and redis connections."""

    await db.ainit()
    await redis.ainit()

@app.middleware("http")
async def attach(request: Request, call_next: Coroutine) -> Response:
    """Attach the databases and redis connections to requests."""

    request.state.db = db
    request.state.redis = redis

    return await call_next(request)
