from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return dict(name="my-awesome-api", version="1.0.0")
