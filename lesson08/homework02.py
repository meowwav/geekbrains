# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider
        
    def divide(self):
        if self.divider == 0:
            raise MyZeroDivisionError
        else:
            return self.dividend / self.divider
        
class MyZeroDivisionError(Exception):
    
    def __str__(self):
        return "Can't divide by zero!"
    
    
while True:
    divider = int(input("Enter the diveder >>> "))
    div = Division(100, divider)
    
    try:
        print(div.divide())
    except MyZeroDivisionError as exception:
        print(exception)