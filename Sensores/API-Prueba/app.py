import pika
import json
from flask import Flask, request

app = Flask(__name__)

# @app.route('/sensor-data', methods=['POST'])
# def sensor_data():
#     # Recibe
#     request.get_json()
#     # Responde con un "ok"
#     return "ok", 200

# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5000, debug=True)


# Conectar con RabbitMQ
def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    return connection

@app.route('/send-data', methods=['POST'])
def receive_sensor_data():
    data = request.json
    sensor_type = data.get("sensor_type")  # Tipo de sensor (ej: temperatura, ocupación, etc.)

    # Establecer conexión con RabbitMQ
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    # Declarar exchange (para distribuir mensajes a diferentes colas)
    channel.exchange_declare(exchange='sensor_exchange', exchange_type='direct')

    # Publicar mensaje en RabbitMQ
    channel.basic_publish(
        exchange='sensor_exchange',
        routing_key=sensor_type,  # Cada sensor tendrá su propia clave de enrutamiento
        body=json.dumps(data)
    )

    connection.close()

    return {"message": "Data sent to RabbitMQ"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

