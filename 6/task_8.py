print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
# Долой инпуты! Времяжорки!

iNumber_X = int(input("Введите число X: "))
iNumber_Y = int(input("Введите число Y: "))
iNumber_P = int(input("Введите число P: "))
iYears = 0
iDepo = iNumber_X
while iDepo < iNumber_Y:
    iYears += 1
    iDepo += int(iDepo / 100 * iNumber_P)
#    print(iDepo, iDepo / 100 * iNumber_P)

print("Прошло много лет. Конекретно:", iYears)
