# Представлен список чисел.
# Непобходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента
from random import randint


my_list = [randint(0, 5) for i in range(10)]
# print(my_list)

new_list = []

for index, element in enumerate(my_list):
    if my_list[index] > my_list[index-1]:
        new_list.append(my_list[index])
   
print(new_list)


