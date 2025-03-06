from flask import Flask, jsonify, request
import time, os


time.sleep(10)

app = Flask(__name__)

"""
    We return the data from the file.
"""

def read_path_file():
    return os.getenv('PATH_FILE_POWER', './data/power.csv')

@app.route('/power', methods=['GET'])
def get_ocupacion():
    with open(read_path_file(), 'r') as file:
        data = file.read()
    return jsonify(data), 200

@app.route('/power', methods=['POST'])
def post_ocupacion():
    # append data to file
    data = request.get_json()
    with open(read_path_file(), 'a') as file:
        file.write(data)
    return jsonify({'status': 'Data saved'}), 200

    
@app.route('/health', methods=['GET']) 
def health():
    return jsonify({'status': 'Healthy'}), 200


    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


