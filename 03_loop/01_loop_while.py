###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0

while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: "))
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")