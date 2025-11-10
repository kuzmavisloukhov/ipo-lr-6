# Kuzma Visloukhov

# Импорт библиотеки
import re

# Описание работы программы
print("Прогрмаа находит строку по введенной пользователем подстроке(с учетом регистра): ")

# Открытие файла
with open("text.txt", "r", encoding="utf-8") as file_text:
    file_text = file_text.read() # Переменная которая читает файл
    user_search_str = [] # Создание пустого списка
    file_text = re.findall(r'[^ \s ! ? \ . ; ... , — -"]+', file_text) # Исключение специальных символов
    file_text = list(filter(None, file_text)) # Исключает определенные элементы
    user_str = input("Введите подстроку для поиска строк в тексте: ") # Запро строки от пользователя

    # Перебор содержимого файла
    for i in file_text:

        # Проверка на существование подстроки пользователя в содержимом файла
        if user_str in i:
            user_search_str.append(i) # Добавляет подсткроу пользователя если она есть в файле
    user_search_str = sorted(user_search_str, key=len) # Сортирует строки по  длине 
    
    # Вывод совпадающих строк
    print(user_search_str)
