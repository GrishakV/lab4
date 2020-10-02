#!usr/bin/env python3
# -*- config: utf-8 -*-

import sys
import math

# Вариант 6
# Решить квадратное неравенство ax^2+bx+c>0 (a != 0), где
# a, b и c - действительные числа.
if __name__ == '__main__':
    print("a * x^2 + b * x + c < 0")
    a = float(input("Введите a: "))
    if a == 0:
        print("a не может быть равно 0", file=sys.stderr)
        exit(1)
    b = float(input("Введите b: "))
    c = float(input("Введите c: "))

    if a > 0:
        dis = b * b - 4 * a * c
        print(f" Дискриминант = {dis}")
        if dis > 0:
            x1 = (-b + math.sqrt(dis)) / (2 * a)
            x2 = (-b - math.sqrt(dis)) / (2 * a)
            if x1 > x2:
                print(f"{x2} < x < {x1}")
            else:
                print(f"{x1} < x < {x2}")
        elif dis == 0:
            x = -b / (2 * a)
            print(f"x != {x}")
        else:
            print("Нет решений")
    elif a < 0:
        print("Умножаем неравенсво на (-1): a * x^2 - b * x - c > 0")
        a *= -1
        b *= -1
        c *= -1
        dis = b * b - 4 * a * c
        print(f" Дискриминант = {dis}")
        if dis > 0:
            x1 = (-b + math.sqrt(dis)) / (2 * a)
            x2 = (-b - math.sqrt(dis)) / (2 * a)
            print(f"x < {x2} and {x1} < x")
        elif dis == 0:
            x = -b / (2 * a)
            print(f"x != {x}")
        else:
            print("Нет решений")
