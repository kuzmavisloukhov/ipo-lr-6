# Kuzma Visloukhov

import random # добавление библиотеки random
import itertools # добавление библиотеки itertools

# Создание счетчика
count_num = 0

# Создание многомерного списка
random_list = [[random.randint(-1, 1) for _ in range(4)] for _ in range(20)]

# Вывод многомерного списка
print(random_list)

# Создание множества
unique_combinations = set()

# Переобор многомерного списка
for unsorted_list in random_list:
    sorted_list = tuple(sorted(unsorted_list)) # Преобразование в кортеж и сортировка
    unique_combinations.add(sorted_list) # Добавляем корьежи в множество

# Преобразуем обратно в список кортежей
unique_combinations = list(unique_combinations)

# Вывод уникальных значений
print("Уникальные значения: ")

# Перебор списка кортежей
for i in unique_combinations:
    print(i) # Вывод каждого кортежа

# Запрос ввода числа
user_num = int(input("Введите целое число: "))

# Перебор списка кортежей и поиск уникальных комбинаций без учета порядка значений
for num1, num2 in itertools.combinations(unique_combinations, 2):

    # Проверка сумм пар на меньшее значение чем число пользователя
    if sum(num1) + sum(num2) < user_num:
        count_num += 1 # Добавление значения к счетчику

# Вывод информации
print(f"Количество пар, чья сумма меньше заданного пользователем значения: {count_num}")