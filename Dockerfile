FROM python:3.9-alpine

RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python3-dev py-pip build-base rust cargo

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY notify.py .

ENTRYPOINT ["python", "/app/notify.py"]