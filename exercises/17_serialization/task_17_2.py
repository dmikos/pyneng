# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
####
import re


def parse_sh_cdp_neighbors(f_data):
    # hostname = re.search('(?P<hn>\w+)>', f_data).group('hn')
    # SW1
    # content: re.search('(\w+) +(\w+ *\w+/\w+) +\d+ +(?:\w )+ +\d+ +(\w+ *\w+/\w+)', f_data).groups()
    # ('R1', 'Eth 0/1', 'Eth 0/0')
    # re.findall('(\w+) +(\w+ *\w+/\w+) +\d+ +(?:\w )+ +\d+ +(\w+ *\w+/\w+)', f_data)
    # [('R1', 'Eth 0/1', 'Eth 0/0'), ('R2', 'Eth 0/2', 'Eth 0/0'), ('R3', 'Eth 0/3', 'Eth 0/0'), ('R4', 'Eth 0/4', 'Eth 0/0')]
    hostname = re.search('(?P<hn>\w+)>', f_data).group('hn')
    res_list = re.findall('(\w+) +(\w+ *\w+/\w+) +\d+ +(?:\w )+ +\S+ +(\w+ *\w+/\w+)', f_data)

    res_dict = {hostname:{}}
    for res_item in res_list:
        res_dict[hostname].update({res_item[1]:{res_item[0]:res_item[2]}})

    return res_dict


if __name__=="__main__":
    f_name = 'sh_cdp_n_sw1.txt'
    with open(f_name) as f:
        print(parse_sh_cdp_neighbors(f.read()))
