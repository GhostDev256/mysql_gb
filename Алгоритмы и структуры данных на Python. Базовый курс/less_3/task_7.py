# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между 
# собой (оба являться минимальными), так и различаться.

import random

r = [random.randint(0, 100) for _ in range(10)]
print(f"Массив: {r}")

min_1 = 10000
min_2 = 10000
for i in r:
    if min_1 > i:
        min_2 = min_1
        min_1 = i
    elif min_2 > i:
        min_2 = i

print(f"Наименьшие элементы: {min_1} и {min_2}")