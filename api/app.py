from flask import Flask, request, jsonify
import pika, json, time, os
import requests


time.sleep(10)

app = Flask(__name__)

"""
    We need to forward the data we receive to RabbitMQ.
    We will use the pika library to interact with RabbitMQ.
    We will also use the json library to convert the data to JSON format.
"""

def read_api_ocupacion():
    return os.getenv('API_OCUPACION', 'http://ocupacion:5000/ocupacion')

def read_api_power():
    return os.getenv('API_POWER', 'http://power:5000/power')

def read_api_temperatura():
    return os.getenv('API_TEMPERATURA', 'http://temperatura:5000/temperatura')

def read_api_seguridad():
    return os.getenv('API_SEGURIDAD', 'http://seguridad:5000/seguridad')




def send_to_queue(data):
    rabbitmq_host = os.getenv('RABBITMQ_HOST')
    rabbitmq_credentials = pika.PlainCredentials(os.getenv('RABBITMQ_USERNAME'),os.getenv('RABBITMQ_PASSWORD'))
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host,credentials=rabbitmq_credentials))
    
    channel = connection.channel()
    channel.queue_declare(queue='data')
    channel.basic_publish(exchange='', routing_key='data', body=json.dumps(data))
    # connection.close()

    
@app.route('/sensor-data', methods=['POST'])
def sensor_data():
    data = request.get_json()
    send_to_queue(data)
    return jsonify({'status': 'Data sent to queue'}), 200


@app.route('/ocupacion', methods=['GET'])
def get_ocupacion():
    response = requests.get(read_api_ocupacion())
    return jsonify(response.json()), response.status_code

@app.route('/power', methods=['GET'])
def get_power():
    response = requests.get(read_api_power())
    return jsonify(response.json()), response.status_code

@app.route('/temperatura', methods=['GET'])
def get_temperatura():
    response = requests.get(read_api_temperatura())
    return jsonify(response.json()), response.status_code

@app.route('/seguridad', methods=['GET'])
def get_seguridad():
    response = requests.get(read_api_seguridad())
    return jsonify(response.json()), response.status_code


@app.route('/health', methods=['GET']) 
def health():
    return jsonify({'status': 'Healthy'}), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


