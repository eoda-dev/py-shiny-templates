# Shiny Templates

## Usage

To use [fastapi-routes](fastapi-routes) template run:

```bash
uv init

uv add shiny

# source .venv/bin/activate

shiny create -g eoda-dev/py-shiny-templates -t fastapi-routes

cd fastapi-routes
uv add -r requirements.txt
shiny run app:app
```

