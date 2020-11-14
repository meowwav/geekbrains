# Реализовать программу работы
# с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение
# и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    n_partition = int
    
    def __init__(self, n_partition):
        self.n_partition = n_partition

# Сложение. Объединение двух клеток. 
# При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
    def __add__ (self, other):
        return self.n_partition + other.n_partition
    
# Вычитание. Участвуют две клетки. 
# Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
    def __sub__(self, other):
        if self.n_partition > other.n_partition:
            return self.n_partition - other.n_partition
        elif other.n_partition > self.n_partition:
            return other.n_partition - self.n_partition
    
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток.
    def __mul__(self, other):
        return self.n_partition * other.n_partition
    
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется
# как целочисленное деление количества ячеек этих двух клеток.
    def __truediv__(self, other):
        if self.n_partition >= other.n_partition:
            return self.n_partition // other.n_partition
        else:
            return other.n_partition // self.n_partition
    
# В классе необходимо реализовать метод make_order(), 
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15,
# количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
    def make_order(self, row):
        self.output = ""
        for patrition in range(self.n_partition // row):
            for i in range(row):
                self.output += "*"
            self.output += "\n"
        if self.n_partition % row != 0:
            for j in range(self.n_partition % row):
                self.output += "*"
        return self.output
    
c1 = Cell(15)
c2 = Cell(45)
c = Cell(c1 + c2)
print(f"c1 + c2 = {c.n_partition}")
print(c.make_order(17))

c = Cell(c1 - c2)
print(f"c1 - c2 = {c.n_partition}")
print(c.make_order(4))

c = Cell(c1 * c2)
print(f"c1 * c2 = {c.n_partition}")
print(c.make_order(30))


c = Cell(c1 / c2)
print(f"c1 / c2 = {c.n_partition}")
print(c.make_order(2))




        
    

