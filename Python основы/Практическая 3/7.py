# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое 
# слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(arg):   
    return print(*[f"{str(i[0]).upper()}{i[1:]}" for i in arg])

int_func(input("Введите что-нибудь: ").split())