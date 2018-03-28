# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
####
def get_int_vlan_map(config_file):
    with open(config_file, 'r') as f:
        dict_access={}
        dict_trunk={}

        for line in f:
            line = line.strip()
            if line.startswith('interface'):
                intf = line.split()[-1]
            if line.startswith('switchport access'):
                vlan = line.split()[-1]
                dict_access[intf]=int(vlan)
            elif line.startswith('switchport trunk allowed'):
                vlans = line.split()[-1]
                dict_trunk[intf]=[int(vlan) for vlan in vlans.split(',')]


    # print(dict_access)
    # print(dict_trunk)
    return dict_access, dict_trunk




res = get_int_vlan_map('config_sw1.txt')
for result in res:
    print(result)