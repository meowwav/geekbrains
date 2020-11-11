# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname,
# position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income = {"wage" : int, "bonus" : int}
               
               
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus   
    
    def get_full_name(self):
        print(f"{self.name} {self.surname}")
        
    def get_total_income(self):
        print("Total income >>> ", self._income["wage"] + self._income["bonus"])
        
junior_developer = Position("Kirill", "Krukov", "Junior Developer", 25000, 5000)

junior_developer.get_full_name()
junior_developer.get_total_income()