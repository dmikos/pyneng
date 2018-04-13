# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
####
# python task_15_3a.py config_r1.txt

import re

def parse_cfg(f_name):
    result_dict = {}
    regex1 = 'interface +(\S+)'
    regex2 = 'ip address ((?:\d+\.)+\d+) +((?:\d+\.)+\d+)'

    with open(f_name, 'r') as f:
        for line in f:
            if re.search(regex1, line.strip()):
                intf = re.search(regex1, line.strip()).group(1)
            elif re.search(regex2, line.strip()):
                result_dict[intf]=re.search(regex2, line.strip()).groups()
    return result_dict


if __name__=='__main__':
    from sys import argv

    f_name = argv[1]
    print(parse_cfg(f_name))
