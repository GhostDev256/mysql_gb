# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, надо вывести 6843.

# Генератор (или листкомпрехеншен) очень напрашивается.
# num = input("Введите число: ")
# print("".join((num[-i] for i in range(1, len(num)+1))))

# Без массива.
res = ""
num = input("Введите число: ")
for i in range(1, len(num)+1):
    res = res + num[-i]

print(res)