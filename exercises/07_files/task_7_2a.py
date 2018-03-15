# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
####
from sys import argv

f_name = argv[1]
with open(f_name, 'r') as f:
    for line in f:
        if not line.startswith('!'):
            flag = True
            for word in ignore:
                if word in line:
                    flag = False
            if flag:
                print(line.strip())
