from htmltools import a
from shiny import App, render, ui


def get_user(session):
    return session.http_conn.session.get("user")


ui = ui.page_fluid(
    ui.panel_title("Hello from your Secure Shiny App!"),
    ui.output_text_verbatim("txt"),
    ui.output_ui("links"),
)


def server(input, output, session):
    @render.ui
    def links():
        if get_user(session) is None:
            return a("login", href="/login")

        return a("logout", href="/logout")

    @render.text
    def txt():
        user = get_user(session)
        if user is None:
            return "Please login to view this page!"

        return f"Hi {user['nickname']}, your email is {user['email']}!"


app = App(ui, server)
