# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('file01.txt', 'w') as text_file:
    while True:
        data = input("(For end - empty string) Enter the string >>> ")
        if data != "":
            text_file.writelines(f"{data}\n")
        else:
            break