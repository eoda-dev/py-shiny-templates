from shiny import App, render, ui


ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)


def server(input, output, session):
    @render.text
    def txt():
        print(session.http_conn.headers["host"])
        return f"n*2 is {input.n() * 2}"


app = App(ui, server)
