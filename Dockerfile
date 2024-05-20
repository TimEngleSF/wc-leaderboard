FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY static/ static/

EXPOSE 8080

COPY .env .env

ENV PYTHONUNBUFFERED=1

CMD ["python", "web/main.py"]
