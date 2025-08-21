# 1. Introducción a las Clases en Python
# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (métodos) en un solo lugar.

import requests


OPENAI_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
DEEPSEEK_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Ejemplo básico de una clase
class Coche:
    # Atributos de la clase (compartido por todas las instancias)
    tipo = "Vehículo de cuatro ruedas"
    ruedas = 4

    # Método especial que construye el objeto
    # se llama automáticamente al crear una instancia de la clase
    def __init__ (self, marca=None, modelo=None, color=None):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} está arrancando... 🚘")

mi_toyoto = Coche("Toyota", "Corolla", "Rojo")
mi_toyoto.arrancar()
print(mi_toyoto.tipo)

mi_potrillo = Coche("Ford", "Mustang", "Azul")
mi_potrillo.arrancar()
print(mi_potrillo.tipo)

# Encapsulación: es ocultar los detalles internos de una clase. y exponer solo la interfaz pública.

# Crear una clase apra llamara la API de OpenAI, DeepSeek, etc.

class AI_API:
    def __init__(self, api_key, url, model):
        self.api_key = api_key
        self.url = url
        self.model = model

    def call(self, prompt):
        url = self.url
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()  # Lanza un error si la respuesta no es exitosa
            res_json = response.json()
            print(res_json["choices"][0]["message"]["content"])
        except requests.exceptions.RequestException as e:
            print(f"Error al llamar a la API: {e}")
            return None
        
# Ejemplo de uso de la clase API
print("\nLlamada a la API de OpenAI:")
openai_api = AI_API(OPENAI_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4o-mini")
openai_api.call("Escribe un breve poema sobre la programación")

print("\nLlamada a la API de DeepSeek:")
deepseek_api = AI_API(DEEPSEEK_API_KEY, "https://api.deepseek.com/chat/completions", "deepseek-chat")
deepseek_api.call("Escribe un breve poema sobre la programación")