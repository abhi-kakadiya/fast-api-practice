FROM python:3.8.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5400

CMD ["bash", "-c", "alembic upgrade head && python3 main.py"]
