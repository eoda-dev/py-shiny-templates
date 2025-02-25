from fastapi import FastAPI
from shiny import App, render, ui
from starlette.applications import Starlette
from starlette.routing import Mount

# ---
app_fastapi = FastAPI()


@app_fastapi.get("/")
def index():
    return dict(name="my-awesome-api", version="1.0.0")


# ---
shiny_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def shiny_server(input, output, session):
    @render.text
    def txt():
        print(session.http_conn.headers["host"])
        return f"n*2 is {input.n() * 2}"


app_shiny = App(shiny_ui, shiny_server)

# ---
routes = [Mount("/api", app=app_fastapi), Mount("/", app=app_shiny)]

app = Starlette(routes=routes)
