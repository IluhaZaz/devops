FROM python:3.11-alpine

RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev libpq

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
