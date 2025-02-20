import json
import requests
from django.utils import timezone
from .models import Logs  # Importa el modelo Logs


# def request_api(endpoint: str, data: dict = None, model=None, method= str):
def request_api(endpoint: str, method: str = "GET", data: dict = None):
    """
    Función genérica para hacer peticiones HTTP y registrar logs.

    Args:
        endpoint (str): La URL del endpoint.
        data (dict, optional): Los datos a enviar en la petición. Defaults to None.
        model: Opcional, para tipado o uso futuro.

    Returns:
        dict: La respuesta de la API.
    """

    try:
        # Hacer la petición HTTP
        if method == "GET":
            response = requests.get(endpoint, params=data)
        elif method == "POST":
            response = requests.post(endpoint, json=data)
        elif method == "PUT":
            response = requests.put(endpoint, json=data)
        elif method == "DELETE":
            response = requests.delete(endpoint)
        else:
            raise ValueError("Método HTTP no válido")

        response_data = response.json()  # Convertir la respuesta a JSON
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{response_data}")
        status_code = response.status_code  # Obtener el código de estado

        # Registrar el log en la base de datos
        log = Logs(
            endpoint=endpoint,
            input_data=json.dumps(data) if data else None,
            output_data=json.dumps(response_data) if response_data else None,
            code=status_code if status_code else None
        )
        log.save()  # Guardar el log en la base de datos

        # Devolver la respuesta de la API
        return response_data

    except requests.exceptions.RequestException as e:
        # Manejar errores de conexión o petición
        error_data = str(e)
        log = Logs(
            endpoint=endpoint,
            input_data=json.dumps(data) if data else None,
            output_data=json.dumps(error_data) if error_data else None,
            code=500  # Código de error genérico
        )
        log.save()
        return error_data
