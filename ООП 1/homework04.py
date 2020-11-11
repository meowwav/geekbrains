# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction)
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from time import sleep

class Car:
    speed = 0
    color = str
    name = str    
    direction = str
    _is_police = bool
    max_speed = int # для лучшей реализцаии
    attention = False
    
    def __init__(self, name, color, max_speed, direction="Forward", _is_police=False):
        self.color = color
        self.name = name
        self.max_speed = max_speed
        self.direction = direction
        self._is_police = _is_police
    
    def go(self):
        if self.attention == False:
            print("Starting engine > > >")
            while self.speed < self.max_speed:
                self.speed += 10
                self.show_speed()
                sleep(1)
            print("MAX SPEED")
            sleep(1)
            self.attention = False
        
    def stop(self):
        if self.speed > 0:
            print("Stopping < < <")
            while self.speed > 0:
                self.speed -= 10
                sleep(0.5)
        print("STOPPED\n")
        sleep(2)
        
    def turn(self, direction):
        self.direction = direction
        print(f"Turned {direction.upper()}")
        sleep(1)
            
    def show_speed(self):
        print(f"Current speed >>> {self.speed}")
        

class TownCar(Car):
    def show_speed(self):
        print(f"Current speed >>> {self.speed}") 
        if self.speed > 60: 
            print("ATTENTION. SLOW DONW!")  
            self.attention = True


class SportCar(Car):
    pass   

class WorkCar(Car):
    def show_speed(self):
        print(f"Current speed >>> {self.speed}") 
        if self.speed > 40: 
            print("ATTENTION. SLOW DONW!")  
            self.attention = True   
  

class PoliceCar(Car):
    pass

police_car = PoliceCar("Lada", "gray", 100, _is_police=True)
print(police_car.color, police_car.name)
police_car.go()
police_car.turn("Left")
police_car.stop()

town_car = TownCar("Renault", "red", 80)
print(town_car.color, town_car.name)
town_car.go()
town_car.turn("Right")
town_car.stop()

work_car = WorkCar("Isuzu", "white", 50)
print(work_car.color, work_car.name)
work_car.go()
work_car.turn("Left")
work_car.stop()

sport_car = SportCar("Mazda RX-8", "BLACK", 220)
print(sport_car.color, sport_car.name)
sport_car.go()
sport_car.turn("Right")
sport_car.stop()