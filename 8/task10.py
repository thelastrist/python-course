print('Задача 10. Кинотеатр')

# X мальчиков и Y девочек пошли в кинотеатр
# и купили билеты на подряд идущие места в одном ряду.
# 
# Напишите программу,
# которая выдаст, как нужно сесть мальчикам и девочкам,
# чтобы рядом с каждым мальчиком сидела хотя бы одна девочка,
# а рядом с каждой девочкой — хотя бы один мальчик.
# 
# На вход подаются два числа - кол-во мальчиков X и кол-во девочек Y.
# В ответе выведите какую-нибудь строку,
# в которой будет ровно X символов “B” (обозначающих мальчиков)
# и Y символов “G” (обозначающих девочек), удовлетворяющую условию задачи.
# Пробелы между символами выводить не нужно.
# Если рассадить мальчиков и девочек согласно условию задачи невозможно,
# выведите строку “Нет решения”.
# 
# 
# Пример 1:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 5
# Ответ: BGBGBGBGBG
# 
# Пример 2:
# 
# Введите кол-во мальчиков: 5
# Введите кол-во девочек: 3
# Ответ: BGBGBBGB
# 
# Пример 3:
# 
# Введите кол-во мальчиков: 100
# Введите кол-во девочек: 1
# Ответ: Нет решения
i, counter, diff, max, min = 0, 0, 0, 0, 0
b_boys = True
out_string = ''
#boys_X = int(input("Enter quantity of boys (X): "))
#girls_Y = int(input("Enter girls quantity (Y): "))

def draw_line(boys_X, girls_Y):
    out_string = ''
    if boys_X / girls_Y > 2 or girls_Y / boys_X > 2:
#        print("No solution")
#        exit(0)
        return("No Solution")

    if boys_X > girls_Y:
        max = boys_X
        min = girls_Y
        b_boys = True
    else:
        max = girls_Y
        min = boys_X
        b_boys = False

    diff = max - min
    for i in range(1, min + 1):
        if b_boys:
            out_string += 'BG'
            if diff > 0:
                out_string += 'B'
                diff -= 1
        else:
            out_string += 'GB'
            if diff > 0:
                out_string += 'G'
                diff -= 1
    return out_string

boys_X = 10 # int(input("Enter quantity of boys (X): "))
girls_Y = 10 #int(input("Enter girls quantity (Y): "))
for i in range(1, boys_X):
    for j in range(1, girls_Y):
        out_string=draw_line(i, j)
        print(i, j, out_string)

#print(boys_X, girls_Y, out_string)
