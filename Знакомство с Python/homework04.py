# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

max_numeral = 0
number = int(input("Enter any number >>> "))
counter = 10

while number >= counter:
    if number % counter > max_numeral:
        max_numeral = number % counter
    number = (number - number % counter) // counter

print("Max numeral in your number is", max_numeral)
