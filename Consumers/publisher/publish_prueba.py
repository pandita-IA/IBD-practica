import pika, os, time

time.sleep(20)  # Esperar a que el contenedor de RabbitMQ inicie

# Conexión
rabbitmq_host = os.getenv('RABBITMQ_HOST')
rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'), os.getenv('RABBITMQ_PASSWORD'))
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, credentials=rabbitmq_credentials))
channel = connection.channel()

# Exchange y colas
EXCHANGE_NAME = 'sensor_exchange'
QUEUES = ["occupancy", "power", "security", "temperature"]

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)

# Declarar y enlazar cada cola con el exchange
for queue in QUEUES:
    channel.queue_declare(queue=queue, durable=True)
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue, routing_key=queue)

# Simulación de envío de mensajes a diferentes colas
messages = {
    "occupancy": "Occupancy data",
    "power": "Power consumption data",
    "security": "Security alert",
    "temperature": "Temperature reading"
}

while True:
    for queue, message in messages.items():
        channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=queue, body=message)
        print(f" [x] Sent '{message}' to {queue}")
    time.sleep(1)

connection.close()
