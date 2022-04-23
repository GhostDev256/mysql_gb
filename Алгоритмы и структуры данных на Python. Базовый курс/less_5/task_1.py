from collections import namedtuple

comp = namedtuple("Company", ["name", "quarters", "profit"])
all_com = set()
total_profit = 0

num_comp = int(input("Количество предприятий: "))

for i in range(1, num_comp+1):
    profit = 0
    quarters = []
    name = input(f"Название предприятия {i}: ")

    for j in range(4):
        quarters.append(float(input(f"Прибль за {j+1} квартал: ")))
        profit += quarters[j]

    com = comp(name=name, quarters=tuple(quarters), profit=profit)
    all_com.add(com)
    total_profit += profit

average = total_profit/num_comp

print(f"\nСредняя прибыль: {average}")
print("-----------------")
print(f"Выше среднего: ")
for com in all_com:   
    if com.profit > average: 
        print(f"Компания {com.name} заработала {com.profit}")

print(f"Ниже среднего: ")
for com in all_com:   
    if com.profit < average: 
        print(f"Компания {com.name} заработала {com.profit}")