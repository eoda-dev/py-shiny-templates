from starlette.applications import Starlette
from starlette.routing import Mount

from app_fastapi import app as app_fastapi
from app_shiny import app as app_shiny
from app_shiny2 import app as app_shiny2

routes = [
    Mount("/another-app", app=app_shiny2),
    Mount("/api", app=app_fastapi),
    Mount("/", app=app_shiny),
]

app = Starlette(routes=routes)
