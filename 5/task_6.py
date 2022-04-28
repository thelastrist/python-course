print('Задача 6. Защита от дурака')

# Мы участвуем в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел,
# и нам необходимо написать этакую «защиту от дурака».
# 
# 
# Напишите программу,
# которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными.
# Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.

#iPlace = int(input("Введите место в списке поступающих:"))
iNumber = int(input("Введите число:"))

print (iNumber // 10)
if ((iNumber // 10) > 0 and (iNumber // 10) < 10) or \
            ((iNumber // 10) > -11 and (iNumber // 10) < -1):
    print(iNumber, " - двузначное число")
else:
    print(iNumber, " - недвузначное число")
