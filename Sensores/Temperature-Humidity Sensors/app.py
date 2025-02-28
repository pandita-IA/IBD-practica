import time
import random
import requests

def read_api_url():
    # Lee la URL desde el archivo 'api_url.txt'
    with open("/app/api_url.txt", "r") as f:
        return f.read().strip()

def simulate_sensor():
    temperature = round(random.uniform(15.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 80.0), 2)
    air_quality = random.choice(["low", "medium", "high"])
    
    data = {
        "temperature": temperature,
        "humidity": humidity,
        "air_quality": air_quality
    }
    return data

if __name__ == "__main__":
    url = read_api_url()
    while True:
        sensor_data = simulate_sensor()
        try:
            response = requests.post(url, json=sensor_data)
            print(f"Enviando datos: {sensor_data} | Respuesta: {response.status_code}")
        except Exception as e:
            print("Error al enviar datos:", e)
        time.sleep(30)  # 30 segundos
