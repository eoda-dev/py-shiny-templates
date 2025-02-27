import json
import base64
import uvicorn
from shiny import App, render, ui

def get_headers(session):
    return session.http_conn.headers

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.output_text_verbatim("principal"),
)


def server(input, output, session):
    @render.text
    def principal():
        headers = get_headers(session)
        client_principal = get_headers(session).get("x-ms-client-principal")
        if client_principal:
            principal = json.loads(base64.b64decode(client_principal))
            return principal
        
        return json.dumps({"x-ms-client-principal": "not submitted"} | dict(headers), indent=2)
    
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

if __name__ == "__main__":
    uvicorn.run(app, port=8000)