# Práctica I IBD

Escritura :: Grupo de Contenedores: Sensores -> Contenedor: API -> Exchange: RabbitMQ -> Cola -> Consumidores: Contenedor
Lectura :: API -> Contenedor

Pasos:


1. Sensor:
    - Crea un dato
    - POST a la API

2. API:
    - forward a RabbitMQ
    - GET /datos

3. RabbitMQ:
    - Recibe el dato
    - Lo pone en la cola

4. Contenedor:
    - Recibe el dato y lo escribe 

GET /temperatura/
GET /tempratura/{fecha}




