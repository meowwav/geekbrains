# Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников
# и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

def average(salary_dict):
    salary_list = []
    for emploee in salary_dict:
        salary_list.append(salary_dict[emploee])
    return sum(salary_list) / len(salary_list)


def less_than(salary_dict, amount):
    less_list = []
    for emploee in salary_dict:
        if salary_dict[emploee] < amount:
            less_list.append([emploee])
    return less_list


salary_dict = {}

with open('file03.txt', 'r', encoding='utf-8') as text_file:
    text_list = text_file.readlines()
    
# наполняем словарь
# salary_dict = {
#     "surname" : salary   
# }
for string in text_list:
        salary_dict.update({string.split()[0] : int(string.split()[1])})



print(f"Average emploees salary is {average(salary_dict)}")
print(less_than(salary_dict, 20000))