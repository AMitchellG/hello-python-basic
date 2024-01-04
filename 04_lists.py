# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [24, 35, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.70, "Andrew", "Mitchell"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list[-3])
print(my_other_list.count("Andrew"))
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(age)
print(height)
print(name)
print(surname)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)
print(height)
print(name)
print(surname)

print(my_list + my_other_list)
# print(my_list - my_other_list) Error

my_other_list.append("AMitchellG")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

# my_list.pop() -Elimina el ultimo elemento de la lista
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))

