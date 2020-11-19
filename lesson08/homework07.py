# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    real_part: int
    complex_part: int
    
    def __init__(self, real_part, complex_part):
        self.real_part = real_part
        self.complex_part = complex_part
        
        
    def __str__(self):
        if self.complex_part > 0:
            return f"{self.real_part}+{self.complex_part}i"
        else: 
            return f"{self.real_part}{self.complex_part}i"
        
    def __add__(self, other):
        rp = self.real_part + other.real_part
        cp = self.complex_part + other.complex_part
        return Complex(rp, cp)
    
    def __mul__(self, other):
        rp = self.real_part * other.real_part
        cp = self.complex_part * other.complex_part
        return Complex(rp, cp)
    
        
        
z1 = Complex(-3, 4)
z2 = Complex(4, -3)

print(z1)
print(z2)
print(z1+z2)
print(z1*z2)