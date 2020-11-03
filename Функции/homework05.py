# Программ запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии на ENTER должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать ENTER
# Сумма вновь введеных числе будет добавляться к уже подсчитанной сумме.
# Но если в место числа будет вводится специальный символ,
# выполнение программы завершается.
# Если специальный символ введе после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу

checker = True  # при получении на ввод "\q" прекращает основной цикл
result = 0

# специальный символ "\q"


def check(check_list):
    """проверяет лист на специальный символ и удаляет "мусор"

    Args:
        check_list ([list]): [entry values]

    Returns:
        [list, int]: [if \q - returns index, else return list without strings]
    """
    global checker
    for element in list(check_list):
        # проверка списка на "\q" и "мусор"
        try:                                            
            float(element)
        except ValueError:
            if element == "\q":
                checker = False
                return check_list.index(element)
            else:
                check_list.remove(element)
    return check_list


def summary(input_list): 
    """Суммирует входящий поток чисел, преобразуя их в лист

    Args:
        input_list ([string]): [входная строка]

    Returns:
        [float]: [сумма потока чисел]
    """
    check_list = input_list.split()
    try:
        return sum(map(float, check_list))
    except ValueError:
        q = check(check_list)
        if checker:
            return sum(map(float, q))
        else:
            return sum(map(float, check_list[0:q]))


while checker:
    print("Для выхода введите \"\q\" ")
    input_list = input("Введите числа через пробел >>> ")
    result += summary(input_list)
    print(result)
print("test")
