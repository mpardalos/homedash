from datetime import datetime, timezone
from pathlib import Path
import asyncio

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sse_starlette import EventSourceResponse, ServerSentEvent


PACKAGE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=PACKAGE_DIR / "templates")


services = {
    'Jellyfin': {
        'url': 'https://jellyfin.home.mpardalos.com',
        'icon': 'https://jellyfin.home.mpardalos.com/web/favicon.bc8d51405ec040305a87.ico'
    },
    'Seerr': {
        'url': 'https://seerr.home.mpardalos.com',
        'icon': 'https://seerr.home.mpardalos.com/favicon-32x32.png'
    },
    'Sonarr': {
        'url': 'https://sonarr.home.mpardalos.com',
        'icon': 'https://sonarr.home.mpardalos.com/favicon.ico'
    },
    'Radarr': {
        'url': 'https://radarr.home.mpardalos.com',
        'icon': 'https://radarr.home.mpardalos.com/favicon.ico'
    },
    'Prowlarr': {
        'url': 'https://prowlarr.home.mpardalos.com',
        'icon': 'https://prowlarr.home.mpardalos.com/favicon.ico'
    },
    'Torrents': {
        'url': 'https://torrents.home.mpardalos.com',
        'icon': 'https://torrents.home.mpardalos.com/transmission/web/images/favicon.svg'
    },
    'Miniflux': {
        'url': 'https://miniflux.home.mpardalos.com',
        'icon': 'https://miniflux.home.mpardalos.com/favicon.ico'
    },
    'Donetick': {
        'url': 'https://donetick.home.mpardalos.com',
        'icon': 'https://donetick.home.mpardalos.com/logo.svg'
    }
}


async def syslog(request: Request) -> Response:
    unit = request.query_params.get('unit')
    unit_arg = f'-u {unit}' if unit else ''

    async def tail_syslog():
        proc = await asyncio.create_subprocess_shell(
            f"journalctl -f {unit_arg}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        async for line in proc.stdout:
            yield ServerSentEvent(
                id='syslog',
                data=line.decode('utf-8').strip()
            )

    return EventSourceResponse(tail_syslog())


async def homepage(request: Request) -> Response:
    return templates.TemplateResponse(
        request,
        "index.html",
        {'services': services}
    )


async def health(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok"})


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/syslog", syslog),
        Route("/health", health),
        Mount("/static", StaticFiles(directory=PACKAGE_DIR / "static"), name="static"),
    ],
    middleware=[Middleware(GZipMiddleware)],
)
