# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год
# и преобразовыватьих тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

# Не сделано:
# Проверка количество дней в месяце в зависимости от месяца,
# также зависимость количества дней в феврале от года
# >>> валидация данных условная

class Date:
    def __init__(self, raw_date):
        self.raw_date = raw_date
        date = Date.extracting(self.raw_date)
        print(Date.validate(date))
    
    @classmethod
    def extracting(cls, raw_date):
        day, month, year = map(int, raw_date.split("-"))
        return {
            "day" : day,
            "month" : month,
            "year" : year
        }
    
    @staticmethod
    def validate(date):
        if date["day"] > 31:
            return "day error"
        elif date["month"] > 12:
            return "month error"
        elif date["year"] > 2020:
            return "year error"
        else:
            return "All right!"

text = Date("25-12-2021")

# TODO 
# валидацию количество дней для каждого месяца + високосный год