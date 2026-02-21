import requests

def request_info():
    url = 'http://localhost:8080/api/info'
    response = requests.get(url)
    return response.json()


def request_sumar(a, b):
    url = 'http://localhost:8080/api/sumar'
    data = {
        'a': a,
        'b': b
    }
    response = requests.post(url, json=data)
    return response.json()

respuesta = request_sumar(5, 10)
print(f'La suma de 5 y 10 es: {respuesta["resultado"]}')