# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

r = [random.randint(0, 100) for _ in range(10)]
print(f"Массив: {r}")

max = -10000
min = 10000

for i in r:
    if i > max:
        max = i
    else:
        min = i

min_index = r.index(min)
max_index = r.index(max)
r[min_index], r[max_index] = r[max_index], r[min_index]
print(f"Мезультат {r}")