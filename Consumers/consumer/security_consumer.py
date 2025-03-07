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

# Colas
QUEUE_NAME = "security"
channel.queue_declare(queue=QUEUE_NAME, durable=True)

CSV_FILE = f"../data/{QUEUE_NAME}.csv"
def callback(ch, method, properties, body):
    data = json.loads(body)
    # Para ignorar header:
    data_filtered = {key: value for key, value in data.items() if key != "header"}
    print(f"Received: {data_filtered}")
    
    # Guardar en CSV
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data_filtered.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data_filtered)

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Ejecución
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)
print(f' [*] Waiting for messages at queue "{QUEUE_NAME}". To exit press CTRL+C.')
channel.start_consuming()