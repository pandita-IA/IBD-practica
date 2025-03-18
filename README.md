# Práctica I IBD

** La version v1.0.0 emplea nuestras imagenes propias del docker hub**

** La version v1.0.0.0 no emplea imágenes propias**

## Integrantes
- **Xuerong**
- **Rafia**
- **Yingying**


## Descripción
En esta práctica el objetivo es crear una infraestructura escalable para gestionar los datos que recibimos de unos sensores. Para ello se ha decidido utilizar una api rest que se encargara de forwardear los datos a rabbitmq para organizarlos por cola para posteriormente ser escritos en un csv. En cuanto a las lecturas hemos decidido crear un api que nos permita leer los datos de los csv y responde a las peticiones de la api rest.


Escritura :: Grupo de Contenedores: Sensores -> Contenedor: API -> Exchange: RabbitMQ -> Cola -> Consumidores: Contenedor 

Lectura :: API -> Contenedor

Pasos:

    Sensor:

        - Crea un dato
        - POST /sensor-data : hacemos un post con los datos a la API con header identificador

    
    API:
        
        - POST /sensor-data : Recibe los datos y los envia a RabbitMQ con el header identificador ya puesto en cada cola
        - GET /ocupacion : Devuelve los datos de la ocupacion
        - GET /power : Devuelve los datos de la potencia
        - GET /temperatura : Devuelve los datos de la temperatura
        - GET /seguridad : Devuelve los datos de la seguridad
        - GET /health : Devuelve el estado de la API
    
    RabbitMQ:

        - Recibe el dato en las colas y lo envia a los consumidores

    Consumidores:
    
        - Poseemos una api para mejor escalabilidad
        - POST /occupancy : escribe los datos en el csv de ocupacion
        - POST /power : escribe los datos en el csv de potencia
        - POST /temperature : escribe los datos en el csv de temperatura
        - POST /security : escribe los datos en el csv de seguridad
        - GET /occupancy : Devuelve los datos de la ocupacion
        - GET /power : Devuelve los datos de la potencia
        - GET /temperature : Devuelve los datos de la temperatura
        - GET /security : Devuelve los datos de la seguridad


To execute the project, you need to have docker and docker-compose installed and run the following command:

```bash
bash setup.sh
```

We are using not the images hosted in docker hub.

In case there is problems with the containers try to **restart the api container**.


## Next steps

Use args for changing the temporal logic of the sensors and have them in separated csvs
