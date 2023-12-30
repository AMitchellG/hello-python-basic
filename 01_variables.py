# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)
# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea ¡Cuidado, esto es mala practica!
name, surname, alias, age = "Andrew", "Mitchell", "AMitchellG", 24
print("Me llamo:", name, surname, ". Mi alias es:", alias, ". Y mi edad es:" , age)

# Inputs
'''
name = input('¿Cuál es tu nombre? ')
age = input('¿Qué edad tienes? ')
print(name)
print(age)
'''

# Cambiamos el tipo a las variables
name = 24
age = "Andrew"
print(name)
print(age)

# ¿Forzamos el tipo de variable? Spoiler: No
address: str = "Mi dirección"
address = 42
address = True
address = 1.2
print(address)