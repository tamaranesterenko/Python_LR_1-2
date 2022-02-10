# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def get_worker():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    date = input("Дата: ")

    return {
        'surname': surname,
        'name': name,
        'zodiac': zodiac,
        'date': datetime.strptime(date, "%Y-%m-%d")
    }

