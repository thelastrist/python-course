print('Задача 1. Пропавшая переменная')
# Что нужно сделать
# Найдите в программе необъявленную переменную и объявите её, присвоив ей значение ‘Кот’.

client = 'Петя'
pet = 'Кот'
print(client)
print(' и ')
print(pet)

print('\nЗадача 2. Цвета')

# Что нужно сделать
# Исправьте программу так, чтобы в результате её выполнения
# на экран в одну строку выводился текст: Red Blue Green RedGreenBlue Blue GreenBlue.
r = 'Red'
g = 'Green'
b =  'Blue'
print(r, b, g, r + g + b, b, g + b)

print('\nЗадача 3. Животные')

# Что нужно сделать
# Создайте две переменные с именами «Первое животное» и «Второе животное» на английском языке. 
# Запишите в первую переменную слово «Заяц», а во вторую — «Черепаха». 
# Используя эти переменные, выведите на экран текст «Заяц спит, Черепаха идёт» в одну строку.

first_animal, second_animal = 'Заяц', 'Черепаха'
print(first_animal, 'спит,', second_animal, 'идёт')

print('\nЗадача 4. Информация о пользователе')
firstname=input('Введите имя: ')
lastname=input('Введите фамилию: ')
city=input('Введите город проживания: ')

print('==============\nВас зовут:', firstname, lastname,'\nВы живёте в городе', city)

print('Задача 5. Вход в систему')

# Что нужно сделать
# Исправьте программу и допишите необходимые команды для получения нужного результата.
# Будьте внимательны при исправлении и помните о правилах названия переменных.

# Программа:

firstname = input('Введите имя пользователя: ')
greeting = 'Утро доброе'
intro = "К сожалению, у Вас нет доступа к системе.\n"
info = "Пожалуйста, обратитесь к системному администратору."
print(greeting, firstname)
print(intro, info)