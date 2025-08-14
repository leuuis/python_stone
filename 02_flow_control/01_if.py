###
# 01 - Sentencias condicionales (if, elif, else)
# Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

import os

os.system("clear")

print("\n Sentencia simple condicional")
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("Felicidades!")


print("\n Sentencia condicional con else")
edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


print("\n Sentencia condicional con else if")
nota = 5
if nota >= 7:
    print("Sobresaliente!")
elif nota >= 8:
    print("Notable!")
elif nota >=5:
    print("No estás muy bien")
else :
    print("No está calificado") #El último else no es obligatorio


print("\n Condiciones multiples")
edad = 25
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir 🚗")
else:
    print("POLICIA 🚔!!!")


# Un pueblo con corrupción
if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla 🚗")
else:
    print("Paga al policia y te deja conducir 🚔!!!")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Venga hay que trabajar!")

print("Anidar condicinonales")
edad = 20
tiene_dinero = True

if edad >= 20: #Anidar mucho procura evitarlo, no es recomendable porque la lógica es mayor y prefiere siempre lo simple
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quédate en casa")
else:
    print("No puedes entrar a la disco")

#Podrias hacerlo mejor así
if edad < 18:
    print("No puedes entrar a la disco")
elif tiene_dinero:
    print("Puedes ir a la discoteca")
else:
    print("Quédate en casa")
