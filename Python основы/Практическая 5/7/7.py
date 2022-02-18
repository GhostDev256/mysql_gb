# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: 
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

average_profit = {"average_profit": 0}
sum_profit = 0

firm_data = {}
with open("text1.txt", "r", encoding="utf-8") as file:
    for j, i in enumerate(file):
        name_firm, form_ownership, revenue, costs = i.split()
        firm_data[name_firm] = int(revenue) - int(costs) # Сказано просто не включать в среднюю прибль, а указать значение.

        if int(costs) > int(revenue):
            sum_profit += 0
        else: 
            sum_profit += int(revenue) - int(costs)

        average_profit["average_profit"] = int(sum_profit/(j+1))     

firm_data["average_profit"] = average_profit.get("average_profit")

with open("res.json", "w") as file:
    json.dump(firm_data, file)