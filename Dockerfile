FROM python:3.9-alpine

RUN apk add --no-cache --virtual build-base gcc musl-dev python3-dev libffi-dev openssl-dev cargo

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY notify.py .

ENTRYPOINT ["python", "/app/notify.py"]