# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней 
# величины дохода сотрудников.

# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open("text.txt", "r", encoding="utf-8") as file:
            average_salary = 0
            lines = file.readlines()

            for line in lines:
                s_name, salary = line.split()
                salary = float(salary)
                average_salary += salary

                if salary < 20000:
                    print(f"{s_name} {salary}")

            if len(lines) > 0:
                average_salary /= len(lines)
                print(f"Средняя зарплата: {average_salary:.2f}\n")