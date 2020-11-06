# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translation = {
    "One" : ["Один", 1],
    "Two" : ["Два", 2],
    "Three" : ["Три", 3],
    "Four" : ["Четыре", 4]
}

file_dict = {}

with open('file04.txt', 'r', encoding="utf-8") as text_file:
    text_list = text_file.readlines()    

for string in text_list:
    string_list = string.split()
    file_dict.update({translation[string_list[0]][0] : translation[string_list[0]][1]})
    
with open('file04-trasnaltion.txt', 'w', encoding="utf-8") as translated_file:
    for element in file_dict:
        translated_file.writelines(f"{element} - {file_dict[element]}\n")
            
    
