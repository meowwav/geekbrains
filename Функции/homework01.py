# Реализовать функцию, принимающую два числа
# (позиционные аругменты) и выполняющих их деление.
# Числа спрашивать у пользователя,
# Предусмотреть обработку ситуации деления на ноль.

def division(a, b):
    try:
        return f"{a} divided by {b} equals {a / b}"
    except ZeroDivisionError:
        return "I can't divide by zero ..."


# бесконечно запрашиваем делимое и делить,
# пока пользователь не введет int или float

while True:
    try:
        a = float(input("Enter the number to divide >>> "))
        break
    except ValueError:
        print("Enter the INTEGER or FLOAT number!!!")

while True:
    try:
        b = float(input("Enter the divider >>> "))
        break
    except ValueError:
        print("Enter the INTEGER or FLOAT number!!!")

print(division(a, b))