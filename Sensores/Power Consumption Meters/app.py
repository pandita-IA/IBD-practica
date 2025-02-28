import time
import random
import requests



def read_api_url():
    # Lee la URL desde el archivo 'api_url.txt'
    with open("/app/api_url.txt", "r") as f:
        return f.read().strip()

def simulate_sensor():
    power_consumption = round(random.uniform(0.5, 5.0), 3)  # kWh
    voltage = round(random.uniform(110, 240), 2)  # V
    current = round(random.uniform(0.5, 20), 2)  # A
    power_factor = round(random.uniform(0.7, 1.0), 2)  # Factor entre 0 y 1
    
    data = {
        "power_consumption": power_consumption,
        "voltage": voltage,
        "current": current,
        "power_factor": power_factor
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
        time.sleep(5)  # 5 segundos
