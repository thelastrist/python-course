print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
def find_max(iDigit1, iDigit2, iDigit3):
    max = 0
    max_message = ''
    if iDigit1 > iDigit2:
        if iDigit1 > iDigit3:
            max = iDigit1
            max_message = "троечников"
        else:
            max = iDigit3
            max_message = "отличников"
    else:
        if iDigit2 > iDigit3:
            max = iDigit2
            max_message = "хорошиство"
        else:
            max = iDigit3
            max_message = "отличников"
    print("Больше всего", max_message+",", "их: ", max)

            
ppl_number = int(input("Введите число учеников: "))
counter_3, counter_4, counter_5 = 0, 0, 0

for my_counter in range(1, ppl_number + 1):
    grade = int(input("Введите оценку ученика №"+str(my_counter)+":"))
    if grade == 3:
        counter_3 += 1
    elif grade == 4:
        counter_4 += 1
    elif grade == 5:
        counter_5 += 1
    else:
        print("Incorrect value entered. Invalid user, replace and restart me.")

find_max(counter_3, counter_4, counter_5)    


