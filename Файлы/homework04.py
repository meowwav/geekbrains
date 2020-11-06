# Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('file05.txt', 'w') as text_file:
    
    while True:
        input_line = input("Enter numbers divided by spaces >>> ")
        try:
            list(map(int, input_line.split()))
            text_file.writelines(input_line)
            break
        except:
            print("Enter INTEGERS only!\nTry again...")
    

with open('file05.txt', 'r') as text_file:
    print(sum(list(map(int, text_file.readline().split()))))
