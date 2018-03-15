# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
####
u_vlan = input('Enter VLAN number: ')
read_f = 'CAM_table.txt'
list_one = []

with open(read_f, 'r') as rf:
    for line in rf:
        if '.' and u_vlan in line:
            vlan, mac, _, intf = line.split()
            print('{}   {}   {}'.format(vlan, mac, intf))
