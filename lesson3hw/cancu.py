what = input("что делаем? (+): (-): (*): (/): ")

a = float(input('Введите первое число '))
b = float(input('Введите второе число '))

if what == "+":
    c = a + b
    print("результат: " + str(c))
elif what == "-":
    c = a - b
    print("результат: " + str(c))
elif what == "*":
    c = a * b
    print("результат: " + str(c))

elif what == "/":
    c = a/b
    print("результат: " + str(c))

else:
    print("Проверьте знак")



