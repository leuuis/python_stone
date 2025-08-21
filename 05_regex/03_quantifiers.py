###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = r"a*"
match = re.findall(pattern, text)
print(match)

# Ejercicio 1:
# Cuántas palabras tienen de 0 a más de "a" y después una "b" en el texto?

text = "aaaba abab aab ab aaab b ba aa"
pattern = r"\ba*b\w*\b"
match = re.findall(pattern, text)
print(match)

# +: Puede aparecer 1 o más veces
text = "dddd aaa ccc bb casa"
pattern = r"a+\b"
match = re.findall(pattern, text)
print(match)

# ?: Puede aparecer 0 o 1 vez
text = "aaabacb"
pattern = r"a?b"
match = re.findall(pattern, text)
print(match)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
text = "Mi número de teléfono es 688999999 apúntalo vale?"
pattern = r"(\+34 )?\d{9}"
found = re.search(pattern, text)
match = found.group() if found else "No se encontró el número"
print(match)

# {n}: Coincide exactamente con n ocurrencias del patrón
text = "aaabbbccc aa aaaaaaa"
pattern = r"a{3}"
match = re.findall(pattern, text)
print(match) if found else "No se encontró el patrón"

# {n, m}: Coincide con al menos n y como máximo m ocurrencias del patrón
text = "aaabbbccc aa aaaaaaa a u"
pattern = r"a{2,4}"
match = re.findall(pattern, text)
print(match) if match else "No se encontró el patrón"  

# Ejercicio: Encuentra las palabras de mas de 4 a 6 letras en el texto
text = "casa casacasacasa casa56 árbol león murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, text)
print(matches) if matches else "No se encontraron palabras de 4 a 6 letras"

# Ejercicio: Encuentra las palabras que tengan más de 5 letras en el texto
text = "casa fantástico casa56 árbol león murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, text)
print(matches) if matches else "No se encontraron palabras de más de 6 letras"