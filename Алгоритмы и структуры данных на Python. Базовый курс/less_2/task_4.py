# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

num = 1
sum = 0

try:
    for i in range(int(input("Количество элементов n: "))):
        sum += num
        num /= -2

    print(sum)
except:
    print("ОшИбка.")