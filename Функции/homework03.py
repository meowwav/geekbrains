# Реализовать функцию my_func(), 
# Которая принимает три позиционных аргумента,
# И возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    sorted_list = sorted(my_list, reverse=True)
    return int(sorted_list[0]) + int(sorted_list[1])


print(my_func(1, 3, 4))
