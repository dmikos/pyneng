# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
####
from sys import argv

f_name = argv[1]
with open(f_name, 'r') as f, open('config_sw1_cleared.txt', 'w') as fw:
    for line in f:
        if not line.startswith('!'):
            flag = True
            for word in ignore:
                if word in line:
                    flag = False
            if flag:
                fw.write(line.strip()+'\n')
