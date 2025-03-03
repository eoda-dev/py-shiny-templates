import os

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_text_verbatim("hostname"),
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    @render.text
    def hostname():
        return "hostname: " + os.getenv("HOSTNAME", "env var $HOSTNAME not set")


app = App(app_ui, server)
