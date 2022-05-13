print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant = 10000 # int(input("Enter educational grant: "))
expenses = 13000 # int(input("Enter expenses: "))
price_growth = 0.03
months = 10
parents_request = expenses - educational_grant

if expenses < educational_grant:
    print("Invalid user, replace and restart")
    exit(404)

for i in range(1, months):
     parents_request += (expenses + expenses * i * price_growth) - educational_grant
     print("delta = ", (expenses + expenses * i * price_growth) - educational_grant, 
         "exp. growth=", expenses * i * price_growth)


print("Hello parents, send me please", parents_request)
