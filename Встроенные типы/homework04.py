# Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

string_list = input("Введети строку из нескольких слов, разделенных пробелами >>> ").split()

for word in string_list:
    print(word) if len(word) <= 10 else print(word[0:10])