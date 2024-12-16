import requests
from auxiliares.constantes import BASE_URL

def obtener_datos(endpoint):
    """Se realiza una solicitud GET al endpoint"""
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def enviar_datos(endpoint, data):
    """Realiza la solicitud POST para enviar datos al endpoint"""
    url = f"{BASE_URL}/{endpoint}"
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        response.raise_for_status()