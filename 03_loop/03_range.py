###
# 03 - range()
# Permite crear una secuencia de números en el momento que se utilice, durante su delcaración no utiliza espacio en memoria. 
# Puede ser útil para for, pero no solo para eso
###

from os import system
if system("clear") != 0: system("cls")

print("\nrange():")

# nums = range(5)
# print(type(nums))
# print(nums)

# for num in range(10):
#     print(num)

# range(inicio, fin)
# for num in range(5, 10):
#     print(num)

# range(inicio, fin, paso)
# for num in range(0, 10, 2):
#     print(num)

# for num in range(-5, 0):
#    print(num)

# for num in range(10, 0, -1):
#     print(num)

# nums = range(1, 101, 5)
# list_of_nums = list(nums)
# print(list_of_nums)
    
# seria para hacerlo cinco veces
for _ in range(5):
    print("Hacer cinco veces algo desde el for")