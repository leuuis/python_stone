###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

""" Definición de una función

def my_function(parametro1, parametro2, ...):
    # docstring
    # cuerpo de la funcion
    return "Resultado mi función" #opcional
"""

#Ejemplo de una función para imprimir algo en consola
# def saludar():
#     print("Hola!")

#Ejemplo de una función con parametro
# def saludar_a(nombre): # parametro
#     print(f"Hola {nombre}!") # argumento

# saludar_a("Ramón")
# saludar_a("Fabio")
# saludar_a("Yorman")
# saludar_a("André")

# el parámetro es lo que acepta la función, en este caso nombre.
# el argumento es lo que se le pasa a la función como valor, en este caso Ramón, Fabio, Yorman y André.

# Funcioens con más parámetros
# def sumar(a, b):
#     suma = a + b
#     return suma

# print(sumar(12, 3))

# Documentar las funciones con docstring
# def restar(a, b):
#     """Resta dos números y devuelve el resultado"""
#     return a - b

# print(restar.__doc__)
# help(restar)

# parámetros por defecto
# def multiplicar (a, b = 2): return a * b
# print(multiplicar(3))
# print(multiplicar(2,8))

# Argumentos por posición
def describir_persona(nombre, edad, sexo ):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros posicionales
describir_persona("Eli", 34, "masculino")
describir_persona("masculino", "hijo", 34)

# Argumentos por clave
# parametros nombrados
describir_persona(edad=34, nombre="Eli", sexo="masculino")

def describir_a_persona(sexo="masculino", nombre="Eli", edad=25) :
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

describir_a_persona("Masculino", "Ricardo", 26)

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args): 
    suma = 0
    for numero in args :
        suma += numero
    return suma

print(sumar_numeros(1,2,3,4,5,6,7,8,))
print(sumar_numeros(1,2))
print(sumar_numeros(1,2,3,4))

# Argumentos de clave - valor
def mostrar_informacion_de(**kwargs): # key word arguments
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="Francisco", edad=38, sexo="hombre")
print("\n")
mostrar_informacion_de(nombre="Bryan", country="Guatemala", sexo="hombre")
print("\n")
mostrar_informacion_de(nombre="Marco", is_rich=True, sexo="hombre")