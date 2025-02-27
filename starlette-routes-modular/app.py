from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Mount, Route

from app_fastapi import app as app_fastapi
from app_shiny import app as app_shiny
from app_shiny2 import app as app_shiny2


def message(request):
    return JSONResponse(dict(message="Hello from Starlette"))


def awesome(request):
    return HTMLResponse("<h1>We are out here!</h1>")


routes = [
    Route("/awesome", endpoint=awesome),
    Route("/message", endpoint=message),
    Mount("/another-app", app=app_shiny2),
    Mount("/api", app=app_fastapi),
    Mount("/", app=app_shiny),
]

app = Starlette(routes=routes)
