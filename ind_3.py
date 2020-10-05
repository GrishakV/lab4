#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 5
# Одноклеточная амеба каждые три часа делится на 2 клетки. Определить, сколько будет
# клеток через 6 часов.
if __name__ == '__main__':
    amoeba = 1

    for i in range(amoeba, 6, 3):
        amoeba *= 2
        print(f"{amoeba}")
