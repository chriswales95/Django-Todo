FROM python:3

WORKDIR /app
RUN pip install Django 
RUN pip install gunicorn 
RUN set -eux; \
    apt-get update; \ 
    apt-get install -y --no-install-recommends \
    sqlite3 \
    nano \
    zip \
    unzip 

