from flask import Flask, request

app = Flask(__name__)

@app.route('/sensor-data', methods=['POST'])
def sensor_data():
    # Recibe
    request.get_json()
    # Responde con un "ok"
    return "ok", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
