FROM python:3.8-slim
WORKDIR /app
COPY . .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x wait-for-it.sh
