# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


import sys


if __name__ == "__main__":
    x = input("Введите строку: ")
    c = input("Введите символ, который нужно заменить: ")
    h = input("Введите символ, на который заменить: ")
    import fun1 as f
    rep = f.fun1(h, c, x)
    print(rep)
