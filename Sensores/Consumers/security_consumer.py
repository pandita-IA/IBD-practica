import pika
import json
import csv
import os

QUEUE_NAME = "security"
CSV_FILE = f"/csv_data/{QUEUE_NAME}.csv"

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Recibido: {data}")

    # Guardar en CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    ch.basic_ack(delivery_tag=method.delivery_tag)  # Confirmar recepción

# Conectar con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

# Declarar cola
channel.queue_declare(queue=QUEUE_NAME)

# Vincular cola con el exchange
channel.queue_bind(exchange='sensor_exchange', queue=QUEUE_NAME, routing_key=QUEUE_NAME)

print(f"Esperando mensajes en {QUEUE_NAME}...")
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=False)

channel.start_consuming()
