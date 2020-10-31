# Для списка реализовать обмен значений соседних элементов, 
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

swap_list = input("Введите элементы через пробел >>> ").split()
new_list = []

for element in swap_list:
    index = swap_list.index(element)
    if index % 2 == 1: 
        new_list.insert(index - 1, element)
    elif index % 2 == 0:
        new_list.insert(index + 1, element)

print(new_list)