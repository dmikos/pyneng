# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

IP_NET = argv[1:]
IP, MASK = IP_NET[0].split('/')

IP_VAL = [int(i) for i in IP.split('.')]
IP_VAL[3] = 0
IP_TEMPLATE = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}  
{0:>08b}  {1:>08b}  {2:>08b}  {3:>08b}  
'''
print(IP_TEMPLATE.format(*IP_VAL))

MASK_TXT = '1'*int(MASK) + '0'*(32-int(MASK))
MASK_LST = [MASK_TXT[:8], MASK_TXT[8:16], MASK_TXT[16:24], MASK_TXT[-8:]]
MASK_VAL = [int(i, 2) for i in MASK_LST]

MASK_TEMPLATE = '''Mask:
{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}  
{1:<08b}  {2:<08b}  {3:<08b}  {4:<08b}  '''

print(MASK_TEMPLATE.format(MASK, *MASK_VAL))
