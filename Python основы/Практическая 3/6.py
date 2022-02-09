# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(arg):
    return print(arg.title()) # Или return print(str(arg[0]).upper() + arg[1:])

int_func(input("Введите что-нибудь: "))