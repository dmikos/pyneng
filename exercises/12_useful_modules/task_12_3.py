# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
####
from tabulate import tabulate
from itertools import zip_longest

def ip_table(ip_list_true, ip_list_false):
    columns=['Reachable', 'Unreachable']

    ip_list=zip_longest(ip_list_true, ip_list_false)

    print(tabulate(ip_list, headers=columns))


if __name__ == "__main__":
    ip_avalaible = ['10.1.1.1', '10.1.1.2']
    ip_unavailable = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
    ip_table(ip_avalaible, ip_unavailable)
