# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(*arg):
    try:
        if int(float(sorted(arg)[-1])) == float(sorted(arg)[-1]) and int(float(sorted(arg)[-2])) == float(sorted(arg)[-2]):
            return print(int(sorted(arg)[-1]) + int(sorted(arg)[-2]))
        else:
            return print(float(sorted(arg)[-1]) + float(sorted(arg)[-2]))
    except:
        return print("Давай нормально плз.")

my_func(input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: "))