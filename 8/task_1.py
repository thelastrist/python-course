print('Задача 1. Космическая еда')

#Ваш космический корабль потерпел крушение на пустынной планете.
# Еда здесь не растёт, но вы спасли из обломков 100-килограммовый мешок гречки.
# Из прошлого опыта вы знаете,
# что если будете экономно питаться, то у вас будет уходить по 4 килограмма гречки в месяц.
# 
# Чтобы прикинуть гречневый бюджет,
# вы решили написать программу, которая выведет информацию
# о том сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее,
# пока она не закончится.
# Используйте цикл for.

weight = 100
per_month = 4

for i in range(4, weight +1, per_month):
    print("Прошло месяцев:", i // per_month, " должно остаться", weight - i, "кило")
