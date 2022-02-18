# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
word = 0

with open("ТЗ работа хз.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                word += len(line.split())
            print(f"Всего строк {len(lines)} и {word} слов")