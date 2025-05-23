FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt --verbose
RUN apt-get update && apt-get install -y libpq-dev
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev tesseract-ocr


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
