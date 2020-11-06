# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
#
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список. 
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

companies_list = []
average = 0

with open('file06.txt', 'r', encoding="utf-8") as text_file:
    companies = text_file.readlines()
    
for company in companies:
    c = company.split()
    companies_list.append({str(f"{c[1]} {c[0]}") : int(c[2]) - int(c[3])})
    average += int(c[2]) - int(c[3])

companies_list.append({"average_profit" : average/len(companies_list)})

with open('companies.json', 'w', encoding="utf=8") as json_file:
    json.dump(companies_list, json_file)
    