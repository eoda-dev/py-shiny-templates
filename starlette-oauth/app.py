import json

from authlib.integrations.starlette_client import OAuth
from starlette.applications import Starlette
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.routing import Mount

from app_shiny import app as shiny_app

app = Starlette(debug=True)
app.add_middleware(SessionMiddleware, secret_key="!secret")

config = Config(".env")
oauth = OAuth(config)

CONF_URL = "https://gitlab.com/.well-known/openid-configuration"
oauth.register(
    name="gitlab",
    server_metadata_url=CONF_URL,
    client_id=config.file_values["GITLAB_CLIENT_ID"],
    client_secret=config.file_values["GITLAB_CLIENT_SECRET"],
    client_kwargs={"scope": "openid email profile"},
)


@app.route("/")
async def homepage(request):
    user = request.session.get("user")
    print("starlette session", request.session)
    if user:
        data = json.dumps(user)
        print(data)
        html = (
            f'<pre>{user["nickname"]}</pre>'
            '<p><a href="/logout">logout</a></p>'
            '<p><a href="/shiny">shiny</a></p>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="/login">login</a>')


@app.route("/login")
async def login(request):
    redirect_uri = request.url_for("auth")
    print(redirect_uri)
    return await oauth.gitlab.authorize_redirect(request, redirect_uri)


@app.route("/auth")
async def auth(request):
    token = await oauth.gitlab.authorize_access_token(request)
    user = token.get("userinfo")
    if user:
        request.session["user"] = user
    return RedirectResponse(url="/")


@app.route("/logout")
async def logout(request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")


app.routes.append(Mount("/shiny", app=shiny_app))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
