from fastapi import FastAPI
import pkgutil
import importlib
from contextlib import asynccontextmanager

from .database import init_db


def _auto_include_routers(app: FastAPI):
    from . import routers as routers_pkg
    for m in pkgutil.iter_modules(routers_pkg.__path__):
        module = importlib.import_module(f"{routers_pkg.__name__}.{m.name}")
        router = getattr(module, "router", None)
        if router:
            app.include_router(router)


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Pantry API", lifespan=lifespan)
_auto_include_routers(app)


@app.get("/")
def health():
    return {"status": "ok"}
