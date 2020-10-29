# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input("Enter your proceeds >>> "))
costs = int(input("enter your costs >>> "))

if proceeds > costs:
    print("Profit")
    profit = proceeds - costs
    profitability = profit / proceeds
    print("Your profitability is", profitability)
    employees_number = int(input("Enter number of employees >>> "))
    profit_per_employee = profit / employees_number
    print("Profit per employee is", profit_per_employee)

elif proceeds < costs:
    print("Loss")
elif proceeds == costs:
    print("Balanced")