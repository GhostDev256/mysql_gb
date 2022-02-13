# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random

res = []
if input("Хотите ввести элементы самостоятельно? Если да, ставьте '+': ") == "+":
    nums = list(map(int, input("Введите элементы списка через пробел: ").split()))
else: nums = [random.randint(0, 1000) for i in range(13)]

for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        res.append(nums[i+1])

print(f"Список: {nums};\nКонечный результат: {res}")