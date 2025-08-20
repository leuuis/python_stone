###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ejemplo tipico de diccionario

persona = {
    "nombre": "elidev",
    "edad": 34,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@leuuis",
        "instagram": "@leuuis", 
        "facebook": "@eluis",
    },
}

# para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# cambair valores al acceder
persona["nombre"] = "eleuuisdev"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]
print(persona)

# eliminar con recuperación
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario, similar a un merge
a = {"name": "elidev", "age": 25}
b = {"name": "leuuisdev", "es_estudiante": True}

a.update(b) # los valores de "b" se asignaran a "a", si falta alguna clave la agrega, no elimina las que estan de mas en a
print(a)

print("name" in persona) # False
print("nombre" in persona)  # True

# obtener todas las claves
print("\nkeys: ")
print(persona.keys())

# obtener todas los values
print("\nvalues: ")
print(persona.values())

# obtener tanto clave como valor
print("\nitems: ")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")