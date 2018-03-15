# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']
####
# python3 task_7_2c.py config_sw1.txt config_sw1_72c.txt
from sys import argv

f_read = argv[1]
f_write = argv[2]
with open(f_read, 'r') as f, open(f_write, 'w') as fw:
    for line in f:
        flag = True
        for word in ignore:
            if word in line:
                flag = False
        if flag:
            fw.write(line.strip()+'\n')
