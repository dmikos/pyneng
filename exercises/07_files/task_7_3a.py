# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
####
read_f = 'CAM_table.txt'
list_one = []

with open(read_f, 'r') as rf:
    for line in rf:
        if '.' in line:
            vlan, mac, _, intf = line.split()
            list_one.append([vlan, mac, intf])
    #print(list_one)
    list_one.sort()
    #print(list_one)
    for lst in list_one:
        vlan, mac, intf = lst
        print('{}   {}   {}'.format(vlan, mac, intf))
