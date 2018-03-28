# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif line.startswith('switchport mode access'):
                dict_access[intf]=1
            elif line.startswith('switchport trunk allowed'):
                vlans = line.split()[-1]
                dict_trunk[intf]=[int(vlan) for vlan in vlans.split(',')]


    # print(dict_access)
    # print(dict_trunk)
    return dict_access, dict_trunk




res = get_int_vlan_map('config_sw2.txt')
for result in res:
    print('\n', result)
