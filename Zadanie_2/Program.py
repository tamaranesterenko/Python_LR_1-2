# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from work import display_workers, get_worker, select_workers  


if __name__ == '__main__':
    workers = []

    while True:

        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            worker = get_worker()

            workers.append(worker)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            display_workers(workers)

        elif command.startswith('select'):
            selected = select_workers(workers)
            display_workers(selected)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить запись;")
            print("list - вывести список;")
            print("select - список родившихся в один месяц;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print("")

