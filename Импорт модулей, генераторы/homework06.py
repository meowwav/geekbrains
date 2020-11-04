# Реализовать два небольших скрипта:
# а) итератор, генерирующий целый числа, начиная с указанного;
# ю) итератор, повторяющий элементы некоторого списка, определенного заранее;

from itertools import count, cycle

start_a = int(input("[count()] Enter the start number >>> "))
stop_a = int(input("[count()] Enter the end number >>> "))

for i in count(start_a):
    if i > stop_a:
        break
    else:
        print(i)
        
my_list = ["Python", "Go", "Java Script", "C++"]

counter_b = 0
stop_b = int(input("[cycle()] Enter the end point for cycle() >>> "))

for item in cycle(my_list):
    if counter_b > stop_b:
        break
    else:
        print(item)
        counter_b += 1