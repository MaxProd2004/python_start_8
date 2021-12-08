# Задание 1
print("Задание 1")
str_1 = str(input("Введите первую строку: "))
str_2 = str(input("Введите вторую строку: "))
set_1 = set(str_1)
set_2 = set(str_2)
print("\nОбщие буквы для обоих строк: ")
for i in set_1:
    if i in set_2:
        print(i, end = " ")

# Задание 2
from random import randint
print("\nЗадание 2")
multiples_of_3 = []
multiples_of_5 = []
size = randint(50, 101)
for i in range(size):
    randnum = randint(1, 1001)
    if randnum % 3 == 0:
        multiples_of_3.append(randnum)
    if randnum % 5 == 0:
        multiples_of_5.append(randnum)
print("Числа, кратные 3-ем: ", multiples_of_3, "Размер списка: ", len(multiples_of_3))
print("Числа, кратные 5-ти: ", multiples_of_5, "Размер списка: ", len(multiples_of_5))
set_of_multiples_of_3 = set(multiples_of_3)
set_of_multiples_of_5 = set(multiples_of_5)
total_numbers = []
for i in set_of_multiples_of_3:
    if i in set_of_multiples_of_5:
        total_numbers.append(i)
print("Общие числа для двух списков: ", total_numbers, end = " ")