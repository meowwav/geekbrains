# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# СДелано:
# Классы, дочерние классы, реализована логистика с отчетами
# Логистика должна хорошо масштабироваться

# Не сделано:
# Валидация данных
# Идея - реализация через классы-исключения

class Warehouse:
    """
    Class for warehouses, also parent class for Office
    """
    name: str
    capacity: int = 10
    current_number: int = 0
    
    storage: dict = {}
    
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

        
    def get(self, name, quantity):
        # отвечает за прием оборудования
        if self.capacity - self.current_number > quantity:
            if name not in self.storage:
                self.storage[name] = quantity
            else:
                self.storage[name] += quantity
            self.current_number += quantity
        print(f"{name} placed at {self.name}")
            
    def move(self, name, quantity, place):
        #отвечает за передачу оборудования
        if name not in self.storage:
            print("There is no this equipment!")
        elif self.storage[name] < quantity:
            print(f"Not enough equipment at {self.name}") 
        else:
                print(f"Moving {name} from {self.name} to {place.name}")
                self.storage[name] -= quantity
                place.get(name, quantity)
                self.current_number -= quantity
        
    
            

    @property        
    def show_storage(self):
        print(f"At {self.name} {self.storage}")
        
class Office(Warehouse):  
    storage: dict = {}
    
    def __init__(self, name, capacity=5):
        self.name = name
        self.capacity = capacity
        

class OfficeEquipment:
    title: str
    model: str
    formats: list
    price: int
    
    count = 0
    
    def __init__(self, title, model, price):
        self.title = title
        self.model = model
        self.price = price
        self.name = f"{model} {title}"
        self.count += 1
        warehouse.get(self.name, 1)
            
    
# оборудование

class Printer(OfficeEquipment):
    ciss: bool
    color_printing: bool
    
    def __init__(self, title, model, price, ciss, color_printing):
        self.title = title
        self.model = model
        self.price = price
        self.name = f"{model} {title}"
        self.ciss = ciss
        self.color_printing = color_printing
        self.count += 1
        warehouse.get(self.name, 1)
        

class Scanner(OfficeEquipment):
    color_scanning: bool
    resolution: int    


class Xerox(OfficeEquipment):
    scanning_speed: int # lists per minute
    xerox_capacity: int
    

warehouse = Warehouse("warehouse", 10)
lubyanka = Office("Lubyanka")
printer = Printer("printer", "samsung", "4000", True, True)
warehouse.show_storage
warehouse.move("samsung printer", 1, lubyanka)
warehouse.show_storage
lubyanka.show_storage
