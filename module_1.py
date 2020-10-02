#!usr/bin/env python3
# -*- config: utf-8 -*-

import math

if __name__ == '__main__':
    x = float(input("Value of x? "))

    if x <= 0:
        y = 2 * x * x + math.cos(x)
    elif x < 5:
        y = x + 1
    else:
        y = math.sin(2 * x) - x * x

    print(f"y = {y}")
