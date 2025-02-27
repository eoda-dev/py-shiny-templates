FROM python:3.11

COPY app.py /opt/shiny/
COPY requirements.txt /opt/shiny

RUN pip install -r /opt/shiny/requirements.txt

EXPOSE 3333

CMD ["gunicorn", "opt.shiny.app:app", "-w 4", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:3333"]

