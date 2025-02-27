FROM python:3.11

RUN pip install -U pip shiny gunicorn

COPY app.py /opt/shiny/app.py

EXPOSE 3333

CMD ["gunicorn", "opt.shiny.app:app", "-w 4", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:3333"]

