import requests
import json

url = "http://127.0.0.1:8000/pedidos/pedidosAPI/9/update_estado/"
headers = {
    "Content-Type": "application/json"
}
data = {
    "estado_pedido": "Nuevo Estado"
}

response = requests.patch(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
