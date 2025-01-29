FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV APP_VERSION=1.0.0
CMD ["python", "app.py"]
