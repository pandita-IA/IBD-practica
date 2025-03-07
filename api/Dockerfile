# Usar la imagen base de Python 3.8
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh

ENTRYPOINT ["./wait-for-it.sh", "rabbitmq:5672", "--", "python", "-u", "app.py"]


CMD ["python", "app.py"]
