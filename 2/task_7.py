print('Задача 7. Путь к файлу')

# Что нужно сделать
# К каждому файлу на компьютере можно узнать путь. Выглядит он примерно так:
# 'C:/user/docs/folder/file_name.txt'

# Напишите программу,
# которая запрашивает у пользователя его имя и имя файла (переменные user и file_name соответственно).
# Используя операцию конкатенации, выведИте путь к файлу на экран.
# Пример результата: 

# Введите ваше имя: Sasha
# Введите имя файла: text
# C:/Sasha/docs/folder/text.txt
username = input("Enter username: ")
filename = input('Enter file name :')
print("C:/"+username+"/docs/folder/"+filename)
