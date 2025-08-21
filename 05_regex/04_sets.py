import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"  # Validar nombre de usuario
match = re.search(pattern, username)
if match:
    print(f"El nombre de usuario {username} es válido", match.group())
else:
    print(f"El nombre de usuario {username} no es válido")

# Buscar todas las vocales en un texto
text = "Hola mundo, ¿cómo estás?"
pattern = r"[aeiouáéíóú]"
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)

# Una Regex para encontrar las palabras man, fan, ban, can, pero ignora el resto
text = "man ran fan ñan ban can dan"
pattern = r"\b[mfb]an\b"
matches = re.findall(pattern, text)
print(matches)

# Podrias validar que sea un rango de edad
text = "22"
pattern = r"[4-9]"
matches = re.search(pattern, text)
print(matches)

# Más rangos pero con letras y dígitos
text = "aZ09"
pattern = r"[a-zA-Z0-9]"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
text1 = "lo.que+sea@shopping.online"
text2 = "michael@gov.co.uk"

pattern = r"^[\w._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
matches1 = re.findall(pattern, text1)
matches2 = re.findall(pattern, text2)
print(matches1)
print(matches2)

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)