# Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции
# возвденения числа в степень

def exp(x, y):
    """решение через оператор **

    Args:
        x ([int, float]): [> 0]
        y ([int, float]): [< 0]

    Returns:
        [float]: [result of expanation]
    """
    return x ** y


def exp_cycle(x, y):
    """решение без оператора **

    Args:
        x ([int, float]): [> 0]
        y ([int, float]): [< 0]

    Returns:
        [float]: [result of expanation]
    """
    if y == 0:
        # любое число в степени 0 дает 1 - это и есть конце нашей рекурсии
        return 1
    else:
        # при новой рекурсии увеличиваем степень на единицу
        return exp_cycle(x, y+1) / x


while True:
    try:
        x = float(input("Enter the positive real number >>> "))
        if x <= 0:
            print("Enter the number > 0")
            continue
        else:
            break
    except ValueError:
        print("Enter the INTEGER or FLOAT number!!!")

while True:
    try:
        y = float(input("Enter the negative real number >>> "))
        if y >= 0:
            print("Enter the number < 0 ")
            continue
        else: 
            break
    except ValueError:
        print("Enter the INTEGER or FLOAT number!!!")

print("\"**\" solution >>>", exp(x, y))

print("Recursive solution >>>", exp_cycle(x, y))