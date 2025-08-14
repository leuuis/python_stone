###
# 02 - Booleanos
# Valores lógicos: True (verdadero) y False (falso).
# Fundamentales para el control de flujo y la lógica en programación.
###

from os import system
if system("clear") != 0: system("cls")

# Los booleanos representan valores de verdad: True o False.
print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

from os import system
if system("clear") != 0: system("cls")

print("\nComparación de cadenas (lexicográficamente):")
print("'manzana' < 'pera':", "manzana" < "pera") # True porque cada caracter tiene un indice asociado en la tabla ASCII y se compara lexicográficamente, no por longitud
print("'Hola' == 'hola'", "Hola" == "hola") # False porque es sensitive case sensible a mayúsculas

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False porque el not invierte
print("not False:", not False)            # True porque el not invierte

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)

numero = 5
if numero: #True
    print("El número no es cero")

numero = 8
if numero == 0: # False
    print("Quí no entrará nunca")

nombre = "Juan"
if nombre:
    print("El nombre no está vacío")

numero = 3 # Adsignación
es_el_tres = numero == 3 #Comparación

if es_el_tres:
    print("El número es el 3")

print("\nLa condición ternaria")
# es una forma concisa de un if-else en una línea de código
# [código si cumple la condición] if [condición] else [código sino cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)