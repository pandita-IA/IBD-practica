import pika
import json
import csv
import os
import time

time.sleep(20)  # Wait for RabbitMQ container to initialize

# Conexión
rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
channel = connection.channel()

# Exchange y colas
EXCHANGE_NAME = 'sensor_exchange'
QUEUE_NAME = "temperature"
channel.queue_declare(queue=QUEUE_NAME, durable=True)

CSV_FILE = f"/csv_data/{QUEUE_NAME}.csv"
def callback(ch, method, properties, body):
    # data = json.loads(body)
    # print(f"Recibido: {data}")

    # # Guardar en CSV
    # file_exists = os.path.isfile(CSV_FILE)
    # with open(CSV_FILE, mode='a', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=data.keys())
    #     if not file_exists:
    #         writer.writeheader()
    #     writer.writerow(data)

    # ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f" [x] Received {body}")

# Ejecución
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
print(f' [*] Waiting for messages at queue "{QUEUE_NAME}". To exit press CTRL+C.')
channel.start_consuming()
