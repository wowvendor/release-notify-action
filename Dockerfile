FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY check.py .

ENTRYPOINT ["python", "/app/notify.py"]