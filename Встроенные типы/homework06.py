# Реализовать структуру данных «Товары». 
# Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами 
# (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:

# [
#    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#   (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Необходимо собрать аналитику о товарах. 
# Реализовать словарь, в котором каждый ключ — характеристика товара, 
# например название, а значение — список значений-характеристик, 
# например список названий товаров.

# Пример:

# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# test = (
#   [
#        1, {
#            "name" : "Vodka",
#            "price" : 300,
#            "count" : 16,
#            "unit" : "bottles"
#        }
#    ], 
#
#    [
#        2, {
#            "name" : "Snacks",
#            "price" : 100,
#            "count" : 32,
#            "unit" : "packages"
#        }
#    ]
# )

articul = 1
goods = []
checker = ""

while checker.lower() != "n":    

    goods_dict = {
        "name" : input("Enter the name of product >>> "),
        "price" : input("Enter the price of product >>> "),
        "count" : input("Enter the count of product >>> "),
        "unit" : input("Enter the unit of product >>> "),
    }

    goods.append( (articul, goods_dict) )

    articul += 1

    checker = input("Add one more product? Y/N ")

new_dict = {
    "name" : [],
    "price" : [],
    "count" : [],
    "unit" : []
}

print("new_dict")

counter = 0

for articules in goods:

    new_dict["name"].append(goods[counter][1]["name"])
    new_dict["price"].append(goods[counter][1]["price"])
    new_dict["count"].append(goods[counter][1]["count"])
    new_dict["unit"].append(goods[counter][1]["unit"])

    counter += 1

print(new_dict)






    
