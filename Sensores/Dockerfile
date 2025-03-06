# Usar la imagen base de Python 3.8
FROM python:3.8

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# NOTA:
# No copiamos app.py de cada sensor aquí, 
# porque lo montaremos como volumen según el servicio.


