from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Mount, Route

from app_fastapi import app as app_fastapi
from app_shiny import app as app_shiny
from app_shiny2 import app as app_shiny2

INDEX = """<div style='padding: 20px; font-family: ubuntu,sans-serif;'>
<h1>Starlette routes</h1>
<ul>
    <li><a href="/api/docs">FastAPI</a></li>
    <li><a href="/shiny">Shiny app</a></li>
    <li><a href="/shiny2">Another Shiny app</a></li>
    <li><a href="/message">Simple JSON Response</a></li>
    <li><a href="/awesome">Simple HTML Response</a></li>
</ul>
</div>"""


def message(request):
    return JSONResponse(dict(message="Hello from Starlette"))


def awesome(request):
    return HTMLResponse("<h1>We are out here!</h1>")


def index(request):
    return HTMLResponse(INDEX)


routes = [
    Route("/message", endpoint=message),
    Route("/awesome", endpoint=awesome),
    Mount("/shiny2", app=app_shiny2),
    Mount("/api", app=app_fastapi),
    Mount("/shiny", app=app_shiny),
    Route("/", endpoint=index),
]

app = Starlette(routes=routes)
