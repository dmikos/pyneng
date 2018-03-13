# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
####
f_run = False

while not f_run:
	ip = input("Введите IP-адрес в формате '10.0.1.1': ")
	f_run = True
	for oct in ip.split('.'):
		# print("oct = {}".format(oct))
		if not oct.isdigit() or ((int(oct)<0 and int(oct)>255)):
			f_run = False
			break

#print("ip = {}".format(ip))

oct1,oct2, oct3, oct4 = [int(x) for x in ip.split('.')]

if oct1 >= 1 and oct1 <= 223:
	print('unicast')
elif oct1 >= 224 and oct1 <= 239:
	print('multicast')
elif oct1==oct2==oct3==oct4==255:
	print('local broadcast')
elif oct1==oct2==oct3==oct4==0:
	print('unassigned')
else:
	print('unused')
