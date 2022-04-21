# ex 1

a, b, c, d = 1, 2, 3, 4
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
print("Sum = ", a + b)

# ex 2
#c = int(input("Enter third number: "))
#d = int(input("Enter fourth number: "))

r1 =  (c + 5 + (a * b / 4 * b))
r2 = (d - (2 * a**3) / 30) 
r3 = 4 - 1 / 30
print (r1, r2, r3, 2 * r1 * r2)
result = 2 * (c + 5 + a * b / 4 * b) * (d - 2 * a**3 / 30) - 10
print("Answer is:", result)

# ex 3
a = '2'
b = '5'
c = '3'
num = 6 ** int(a) + (7 - int(b)) * int(c)
print(num)