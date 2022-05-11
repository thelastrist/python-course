print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.

letter_length = int(input("Enter length of letter: "))
letter_width = int(input("Enter width  of letter: "))

size = 12
counter = 0

while letter_length > size or letter_width > size:
    if letter_length > size:
        letter_length //= 2
        counter += 1
    if letter_width > size:
        letter_width //= 2
        counter += 1

print("You have to fold the letter in half", counter, "times")
