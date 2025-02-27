from shiny import App, render, ui


ui = ui.page_fluid(
    ui.panel_title("Another Shiny App!"),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @render.text
    def txt():
        return "Hi there"

app = App(ui, server)
