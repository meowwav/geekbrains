# Реализовать класс Matrix (матрица). 
# Обеспечить перегрузку конструктора класса (метод init()), 
# который должен принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

# Далее реализовать перегрузку метода add() 
# для реализации операции сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__ (self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.output = ""
        for line in self.matrix:
            for item in line:
                self.output += f"{str(item)} "
            self.output += "\n"
        return self.output
    
    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += other.matrix[i][j]
                
        self.output = ""
        for line in self.matrix:
            for item in line:
                self.output += f"{str(item)} "
            self.output += "\n"
        return self.output
        
    
m1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

m2 = Matrix ([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

print(m1)
print(m2)

print(m1 + m2)


        