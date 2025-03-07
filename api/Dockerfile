# Usar la imagen base de Python 3.8
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x wait-for-it.sh

