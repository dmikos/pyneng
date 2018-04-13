# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
####
# python task_15_3b.py config_r2.txt

import re

def parse_cfg(f_name):
    result_dict = {}
    regex1 = 'interface +(\S+)'
    regex2 = 'ip address ((?:\d+\.)+\d+) +((?:\d+\.)+\d+)'

    with open(f_name, 'r') as f:
        for line in f:
            if re.match(regex1, line.strip()):
                intf = re.match(regex1, line.strip()).group(1)
                print(intf)
                result_dict[intf]=[]
            elif re.search(regex2, line.strip()):
                result_dict[intf].append(re.search(regex2, line.strip()).groups())
    return result_dict


if __name__=='__main__':
    from sys import argv

    f_name = argv[1]
    print(parse_cfg(f_name))
