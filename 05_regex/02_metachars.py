###
# 02 - Meta caracteres
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###

import re

# 1. El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo,  h0la de neuvo, h0la otra vez"
pattern = "H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
    print(found)
else:
    print("No se ha encontrado el patrón")

text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)
print(matches)

# ---------------
text = "Hola mundo,  h0la de neuvo, h0la otra vez"
pattern = r"H.la" # Hola, H0la, H$la

found = re.findall(pattern, text)

if found:
    print(found)
else:
    print("No se ha encontrado el patrón")

# Cómo usar la barra invertida para anular el significado especial de un símbolo
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."
matches = re.findall(pattern, text)
print(matches)

# \d: coincide con cualquier dígito (0-9)

text = "El nuwmero de teléfono es 123456789"
found = re.findall(r'\d{9}', text)
print(found)


# Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34

text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
pattern = r"\+34 \d{9}"
found = re.search(pattern, text)

if found: print(f"Encontré el número de teléfono {found.group()}")

# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

text = "@@#el_rubius_69"
pattern = r"\w"
found = re.findall(pattern, text)
print(found)

# \s: Coincide con cualquier espacio en blanco, tabulación, salto de línea

text = "Hola mundo\nCómo estás\t"
pattern = r"\s"
found = re.findall(pattern, text)
print(found)

# ^: Coincide con el principio de una cadena

text = "423_name%22" # username
pattern = r"^\w" # validar nombre de usuario
valid = re.search(pattern, text)
if valid:
    print(f"El nombre de usuario {text} es válido")
else:
    print(f"El nombre de usuario {text} no es válido")

phone = "+34 823929228"
pattern = r"^\+\d{1,3} \d{9}"  # Validar número de teléfono de cualquier país
valid = re.search(pattern, phone)
if valid:
    print(f"El número de teléfono {phone} es válido")
else:
    print(f"El número de teléfono {phone} no es válido")

# $: Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"  # Validar que la cadena termina con "mundo"
valid = re.search(pattern, text)
if valid:
    print(f"La cadena {text} es válida")
else:
    print(f"La cadena {text} no es válida")

# EJERCICIO
# Valida que un correo sea de gmail
text = "mi_correo16@gmail.com"
pattern = r"^[\w.-_]+@gmail\.com$"  # Validar correo de Gmail
valid = re.search(pattern, text)
if valid:
    print(f"El correo {text} es válido")
else:
    print(f"El correo {text} no es válido")

# EJERCICIO:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt
files = "_file-1.txt file2.pdf midu-of.webp 0secret.txt"
pattern = r"[\w_-]+\.txt"  # Validar archivos con extensión .txt
found = re.findall(pattern, files)
if found:
    print(f"Los archivos con extensión .txt son: {found}")
else:
    print("No se encontraron archivos con extensión .txt")

# Coincidir con el principio y final de una palabra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"  # Coincidir con la palabra "casa" completa
found = re.findall(pattern, text)
print(found)

# |: Coincidr con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"aguacate|palta|p..a|\bw{7}\b"  # Coincidir con "aguacate" o "palta"
found = re.findall(pattern, fruits)
if found:
    print(f"Las frutas encontradas son: {found}")
else:
    print("No se encontraron las frutas especificadas")