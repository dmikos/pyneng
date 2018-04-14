# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
####
import re


def parse_sh_ip_int_br(f_name):
    result = list()
    with open(f_name) as f:
        for line in f:
            regex = re.compile('(?P<intf>\S+ther\S+) +'
                '(?P<ip>(?:(?:\d+\.)+\d+)|unassigned) +'
                '(?P<stat>\w+) +'
                '(?P<method>manual|unset) +'
                '(?P<status>up|administratively down) +'
                '(?P<protocol>\S+)')
            match = regex.search(line.strip())
            if match:
                result.append(match.group('intf', 'ip', 'status', 'protocol'))
    return result


if __name__=="__main__":
    res = parse_sh_ip_int_br('sh_ip_int_br_2.txt')
    print(res)
