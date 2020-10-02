#!usr/bin/env python3
# -*- config utf-8 -*-

import sys

# Вариант 2
if __name__ == '__main__':
    m = int(input("Введите номер месяца: "))

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print("31 день")
    elif m == 2:
        print("28 или 29 дней")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print("30 дней")
    else:
        print("Столько месяцев нема", file=sys.stderr)
    exit(1)
