from flask import Flask, request, jsonify
import pika, json, time, os

app = Flask(__name__)

"""
    We need to forward the data we receive to RabbitMQ.
    We will use the pika library to interact with RabbitMQ.
    We will also use the json library to convert the data to JSON format.
"""

def send_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='data')
    channel.basic_publish(exchange='', routing_key='data', body=json.dumps(data))
    connection.close()

    
@app.route('/sensor-data', methods=['POST'])
def sensor_data():
    data = request.get_json()
    send_to_queue(data)
    return jsonify({'status': 'Data sent to queue'}), 200

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='data')
    method_frame, header_frame, body = channel.basic_get(queue='data')
    if method_frame:
        data = json.loads(body)
        return jsonify(data), 200
    else:
        return jsonify({'data': 'No data in queue'}), 200

@app.route('/health', methods=['GET']) 
def health():
    return jsonify({'status': 'Healthy'}), 200



    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)


