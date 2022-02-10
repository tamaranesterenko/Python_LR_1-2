# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def select_workers(staff):
    month1 = int(input("Введите месяц: "))
    result = []
    for worker in staff:
        if worker.get('date', '').month == month1:
            result.append(worker)
    return result

