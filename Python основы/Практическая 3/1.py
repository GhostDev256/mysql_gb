# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division():
    try:
        return print(float(input("Введите первое число: ")) / float(input("Введите второе число: ")))
    except:
        return print("А это как? Давай норм.")

division()

# Или
#def division(a, b):
#    try:
#        return print(float(a) / float(b))
#    except:
#        return print("А это как? Давай норм.")
#
#division(input("Введите первое число: "), input("Введите второе число: "))