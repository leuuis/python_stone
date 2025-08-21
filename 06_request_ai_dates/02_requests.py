# Cómo hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (díficil y sin dependencias)
import urllib.request
from urllib.error import HTTPError
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_posts)

    if response.status == 200:
        data = response.read()
        json_posts = json.loads(data.decode("utf-8")) # Decodificar bytes a str y luego cargar JSON
        print(json_posts)
    else:
        print(f"Error en la petición: {response.status}")

    response.close()
except urllib.error.URLError as e:
    print(f"Error en la conexión: {e.reason}")

# 2. Con dependencia requests (fácil y con dependencias)
# instalar en consola % pip3 install requests --break-system-package
import requests

print(f"\nGET:")
api_posts_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts_url)
if response.status_code == 200:
    json_posts = response.json()  # Parsear JSON directamente
    print(json_posts)
    print(json_posts[0])  # Primer post
else:
    print(f"Error en la petición: {response.status_code}")

# 3. POST
print(f"\nPOST:")
api_posts_url = "https://jsonplaceholder.typicode.com/posts"
input = {
    "title": "foo",
    "body": "bar",
    "id": 5,
}

try:
    response = requests.post(url=api_posts_url, json=input)
    print(f"Nuevo post creado: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error en la conexión: {e.reason}")

# 4. Un PUT necesita todo el objeto
print("\nPUT:")
try:
  response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={
      "title": "foo",
      "body": "bar",
    })
  print(response.status_code)
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")