# pip install requests
import requests
import re

url =  'https://www.apple.com/es/shop/buy-mac/macbook-air/15-pulgadas'

response = requests.get(url) # Múy rapido y sencillo, pero no navega, salta captchas, muy manual porque necesita regex
if response.status_code == 200:
    print("¡Conexión exitosa!")
    print("Contenido de la página:")
    html = response.text

    # Regular expressions para extraer información de precio
    price_pattern = r'<span class="rc-segmented-control-caption typography-caption">Desde (.*?)</span>'
    match = re.search(price_pattern, html)

    if match:
        price = match.group(1)
        print(f"Precio encontrado: {price}")
    
    # get the title of the page
    title_pattern = r'<title>(.*?)</title>'
    title_match = re.search(title_pattern, html)

    if title_match:
        title = title_match.group(1)
        print(f"Título de la página: {title}")
        
else:
    print(f"Error al conectar: {response.status_code}")

