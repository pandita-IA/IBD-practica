import time
import random
import requests

def read_api_url():
    # Lee la URL desde el archivo 'api_url.txt'
    with open("/app/api_url.txt", "r") as f:
        return f.read().strip()

def simulate_sensor():
    status = random.choice(["active", "inactive"])
    # Simulación de alerta: en ocasiones no se envía alerta
    alert_options = ["motion detected", "unauthorized person", "abandoned object", None]
    alert = random.choice(alert_options)
    alert_level = random.choice(["low", "medium", "high"]) if alert else None
    
    data = {
        "status": status,
        "alert": alert,
        "alert_level": alert_level
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
        time.sleep(120)  # 2 minutos
