from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Función auxiliar para obtener la ruta del archivo CSV
def get_csv_path(sensor_type):
    paths = {
        "occupancy": os.getenv('PATH_FILE_OCUPACION', './data/occupancy.csv'),
        "power": os.getenv('PATH_FILE_POWER', './data/power.csv'),
        "security": os.getenv('PATH_FILE_SECURITY', './data/security.csv'),
        "temperature": os.getenv('PATH_FILE_TEMPERATURE', './data/temperature.csv'),
    }
    return paths.get(sensor_type)

# Ruta GET para obtener datos de cualquier sensor
@app.route('/<sensor_type>', methods=['GET'])
def get_sensor_data(sensor_type):
    file_path = get_csv_path(sensor_type)
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': f'No data found for {sensor_type}'}), 404

    with open(file_path, 'r') as file:
        data = file.read()
    
    return jsonify({'data': data}), 200

# Ruta POST para agregar datos a cualquier sensor
@app.route('/<sensor_type>', methods=['POST'])
def post_sensor_data(sensor_type):
    file_path = get_csv_path(sensor_type)

    if not file_path:
        return jsonify({'error': f'Invalid sensor type: {sensor_type}'}), 400

    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data received'}), 400

    with open(file_path, 'a') as file:
        file.write(str(data) + '\n')

    return jsonify({'status': f'Data saved to {sensor_type}'}), 200

# Endpoint de salud
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'Healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

