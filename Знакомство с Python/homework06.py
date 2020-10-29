#  Спортсмен занимается ежедневными пробежками.
#  В первый день его результат составил a километров.
#  Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
#  Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#  Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

current_distance = int(input("Enter the first result >>> "))
target = int(input("Enter your target >>> "))

day = 1

while current_distance < target:
    day += 1
    current_distance *= 1.1
    print(f"{day} {current_distance}")

print(f"You will get targeted result at {day} day")