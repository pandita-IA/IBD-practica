import time
import random
import requests
import os

def read_api_url():
    return os.getenv('API_URL', 'http://api-prueba:5000/sensor-data')


def simulate_sensor():
    occupancy = random.randint(0, 50)  # Número de personas
    movement = random.choice([True, False])
    location = f"Zone-{random.randint(1, 5)}"  # ID de zona
    dwell_time = round(random.uniform(0, 10), 2)  # Tiempo de permanencia en minutos
    
    data = {
        "occupancy": occupancy,
        "movement": movement,
        "location": location,
        "dwell_time": dwell_time
    }
    return data

if __name__ == "__main__":
    url = read_api_url() 
    while True:
        sensor_data = simulate_sensor()
        try:
            headers = {"queue": "occupancy"}
            response = requests.post(url, json=sensor_data, headers=headers)
            print(f"Enviando datos: {sensor_data} | Respuesta: {response.status_code}")
        except Exception as e:
            print("Error al enviar datos:", e)
        time.sleep(60)  # 1 minuto
