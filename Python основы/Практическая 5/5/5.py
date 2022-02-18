# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open("text1.txt", "w", encoding="utf-8") as file1:        
    user_input = input("Введите цифры через пробел: ")
    file1.writelines(user_input)
    user_input = user_input.split()

print(f"Результат: {sum(map(int, user_input))}")