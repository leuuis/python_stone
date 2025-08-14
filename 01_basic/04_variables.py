##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

my_name = "Luis"
print(my_name)

age = 32
print(age)

age = 39
print(age)

# Tipado dinámico
name = "Eli"
print(type(name))

name = "34"
print(type((name)))

# Tipado fuerte: Python no realiza conversiones de tipado automático
# print(10 + "2")

print(f"Hola {my_name}, tengo {age + 1} años") # Disponible desde la version 3.6 de Python

# Asignación multiple no recomendada
name, age, city = "Elicané", 32, "Izabal"

# Convenciones de nombres para variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "Ok"

# Python no tiene constantes, solo se pueden simular
MI_CONSTANTE = 3.1416 # UPPER_CASE

# mi-variable = "fail"

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_ind: bool = True # Realmente es una anotacion para documentación no un tipado fuerte
print(is_user_logged_ind)

is_user_logged_ind = 42
print(is_user_logged_ind)