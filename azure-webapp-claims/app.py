import base64
import json

import uvicorn
from shiny import App, render, ui


def get_headers(session):
    return session.http_conn.headers


def get_client_principal(session) -> dict | None:
    client_principal = get_headers(session).get("x-ms-client-principal")
    if client_principal:
        client_principal = json.loads(base64.b64decode(client_principal))
        return client_principal

    return None


def get_claim(claims: list[dict], typ: str):
    return [claim for claim in claims if claim["typ"] == typ][0]


app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_text_verbatim("user"),
    ui.output_text_verbatim("principal"),
)


def server(input, output, session):
    @render.text
    def user():
        client_principal = get_client_principal(session)
        if client_principal:
            username = get_claim(client_principal["claims"], "preferred_username")
            return f"Hi {username}, nice to meet you!"

        return "Hi you, nice to meet you!"

    @render.text
    def principal():
        client_principal = get_client_principal(session)
        if client_principal:
            return json.dumps(client_principal, indent=2)

        headers = get_headers(session)
        return json.dumps(
            {"x-ms-client-principal": "not submitted"} | dict(headers), indent=2
        )

    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
