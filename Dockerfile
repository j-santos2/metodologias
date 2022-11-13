FROM python:3.9-slim-buster

WORKDIR /ultimom 

RUN apt-get update && apt-get -y install libpq-dev gcc

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "./gunicorn_run.sh"]
