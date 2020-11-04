# Представлен список чисел.
# Определить элементы, не имеющие повторений.
# Сформировать итоговый массив чисел, соответстующих требованию.
# Элементы вывести в порядки их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор

from random import randint


my_list = [randint(0, 20) for i in range(15)]
# print(my_list)

new_list = []

for element in my_list:
    if my_list.count(element) == 1:
        new_list.append(element)
        
print(new_list)