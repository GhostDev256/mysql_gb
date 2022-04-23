# У меня примерно такие же задачки в школе, только на паскале. (профиль)

from collections import deque

FOOTING = 16
HEX_NUMBER = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
DEC_NUMBER = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, 
              "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, 
              "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

def sum(first, sec):
    first, sec = first.copy, sec.copy

    if len(sec) > len(first):
        first, sec = sec, first 

    sec.extendleft("0" * (len(first)-len(sec)))
    res = deque()
    in_mind = 0

    while not len(first) == 0:
        first_num, sec_num = DEC_NUMBER[first.pop()], DEC_NUMBER[sec_num.pop()]

        res_num = first_num + sec_num + in_mind

        if res_num >= FOOTING:
            in_mind = 1
            res_num -= FOOTING
        else: in_mind = 0

        res.appendleft(HEX_NUMBER[res_num])

    if in_mind == 1:
        res.appendleft("1")

    return res

def multiplicat(first, sec):
    first, sec = first.copy, sec.copy

    if len(sec) > len(first):
        first, sec = sec, first 

    sec.extendleft("0" * (len(first)-len(sec)))
    res = deque("0")

    while not len(first) == 0:
        sec_num = DEC_NUMBER[sec_num.pop()]

        s = deque("0")
        for i in range(sec_num):
            s = sum(s, first)

        s.extend("0" * (len(first)-len(sec)-1))

        res = sum(res, s)

    return res
a = deque(input("Введите первое число: ").upper())
b = deque(input("Введите второе число: ").upper())

print(list(sum(a, b)))
