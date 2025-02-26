# uvicorn app:app
# curl localhost:8000
# curl localhost:8000 -u "hans:password"
# ---
import base64
import binascii

from starlette.applications import Starlette
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    SimpleUser,
)
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount
from starlette.authentication import requires
from starlette.middleware.sessions import SessionMiddleware


from app_shiny2 import app as shiny_app

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if "Authorization" not in conn.headers:
            return

        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)

@requires("authenticated")
async def homepage(request):
    print(request.session.get('user'), request.user.display_name)
    if request.user.is_authenticated:
        return PlainTextResponse("Hello, " + request.user.display_name)
    return PlainTextResponse("Hello, you")


middleware = [Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())]

routes = [Route("/", endpoint=homepage), Mount("/shiny", app=shiny_app, middleware=middleware)]

app = Starlette(routes=routes, middleware=middleware)
app.add_middleware(SessionMiddleware, secret_key="!secret")
