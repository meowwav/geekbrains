# Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('file02.txt', 'r') as text_file:
    text_list = text_file.readlines()
    print(f"Number of string is {len(text_list)}")
    for index, string in enumerate(text_list, 1):
        print(f"In {index} string {len(string.split())} words")

