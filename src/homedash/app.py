from datetime import datetime, timezone
from pathlib import Path

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


PACKAGE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=PACKAGE_DIR / "templates")


async def homepage(request: Request) -> Response:
    return templates.TemplateResponse(request, "index.html")


async def server_time(request: Request) -> Response:
    return templates.TemplateResponse(
        request, "time.html", {"time": datetime.now(timezone.utc)}
    )


async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/time", server_time),
        Route("/health", health),
        Mount("/static", StaticFiles(directory=PACKAGE_DIR / "static"), name="static"),
    ],
    middleware=[Middleware(GZipMiddleware)],
)
