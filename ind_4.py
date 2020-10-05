#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math
import sys

# Вариант 4
EULER = 0.5772156649015328606
ESP = 1e-10

if __name__ == '__main__':
    x = float(input("Введите х: "))
    if x == 0:
        print("Х не может быть равно 0", file=sys.stderr)
        exit(1)

    a = x * x / 4
    S, n = a, 1

    while math.fabs(a) > ESP:
        a *= (2 * x * n) / (2 * n + 1) ** 2
        S += a
        n += 1

    print(f"Chi{x} = {EULER + math.log1p(math.fabs(x))+ S}")
