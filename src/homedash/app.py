from datetime import datetime, timezone

from pathlib import Path
import asyncio
from pprint import pformat, pprint

from sdbus import DbusFailedError, SdBus, SdBusUnmappedMessageError, sd_bus_open_system
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response, PlainTextResponse
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from sse_starlette import EventSourceResponse, ServerSentEvent
from starlette.types import Message

from homedash.dbus.systemd_interface import OrgFreedesktopSystemd1ManagerInterface
from homedash.dbus.systemd_unit_interface import OrgFreedesktopSystemd1UnitInterface


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


class AlreadySubscribed(DbusFailedError):
    dbus_error_name: str = 'org.freedesktop.systemd1.AlreadySubscribed'


class NoSuchUnit(DbusFailedError):
    dbus_error_name: str = 'org.freedesktop.systemd1.NoSuchUnit'


class SystemD(OrgFreedesktopSystemd1ManagerInterface):
    def __init__(self, bus: SdBus | None = None):
        super().__init__()
        self.bus: SdBus = bus or sd_bus_open_system()
        self._proxify(
            service_name='org.freedesktop.systemd1',
            object_path='/org/freedesktop/systemd1',
            bus=self.bus
        )

    async def get_unit_proxy(self, name: str) -> OrgFreedesktopSystemd1UnitInterface:
        object_path = await self.get_unit(name)

        return OrgFreedesktopSystemd1UnitInterface.new_proxy(
            service_name='org.freedesktop.systemd1',
            object_path=object_path,
            bus=self.bus
        )

    async def ensure_subscribed(self) -> None:
        try:
            await self.subscribe()
        except AlreadySubscribed:
            pass


systemd = SystemD()


async def syslog_event_source(unit: str | None = None) -> EventSourceResponse:
    unit_arg = f'-u {unit}' if unit else ''

    proc = await asyncio.create_subprocess_shell(
           f"journalctl -f {unit_arg}",
           stdout=asyncio.subprocess.PIPE,
           stderr=asyncio.subprocess.PIPE,
    )

    async def tail_syslog():
        async for line in proc.stdout:  # pyright: ignore[reportOptionalIterable]
            yield ServerSentEvent(
                id='syslog',
                data=line.decode('utf-8').strip()
            )

    async def finalize(msg: Message):
        proc.kill()

    return EventSourceResponse(tail_syslog(), client_close_handler_callable=finalize)


async def unit_log(request: Request) -> Response:
    return await syslog_event_source(request.path_params['unit'])


async def system_log(request: Request) -> Response:
    return await syslog_event_source()


async def status(request: Request) -> Response:
    unit_name: str = request.path_params['unit']
    try:
        unit = await systemd.get_unit_proxy(unit_name)
    except NoSuchUnit:
        unit = await systemd.get_unit_proxy(f'{unit_name}.service')

    await systemd.ensure_subscribed()

    async def body():
        last_state = await unit.active_state
        yield ServerSentEvent(id='state', data=last_state)
        async for interface, changed, invalidated in unit.properties_changed:
            if interface == "org.freedesktop.systemd1.Unit":
                _, state = changed['ActiveState']  # pyright: ignore[reportAny]
                assert isinstance(state, str)
                if state != last_state:
                    yield ServerSentEvent(id='state', data=state)
                    last_state = state

    return EventSourceResponse(body())


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
        Route("/service/{unit}/status", status),
        Route("/service/{unit}/log", unit_log),
        Route("/system/log", system_log),
        Mount("/static", StaticFiles(directory=PACKAGE_DIR / "static"), name="static"),
    ],
    middleware=[Middleware(GZipMiddleware)],
)
