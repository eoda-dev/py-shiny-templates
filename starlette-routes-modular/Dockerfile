FROM python:3.11

WORKDIR /opt/shiny 

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3333

CMD ["gunicorn", "app:app", "-w 4", "-k uvicorn.workers.UvicornWorker", "-b 0.0.0.0:3333"]

