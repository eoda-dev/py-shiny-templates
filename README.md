# Shiny Templates

## Usage

```bash
uv init

uv add shiny

# source .venv/bin/activate

shiny create -g eoda-dev/py-shiny-templates -t TEMPLATE_FOLDER

cd TEMPLATE_FOLDER
uv add -r requirements.txt
shiny run app:app
```
