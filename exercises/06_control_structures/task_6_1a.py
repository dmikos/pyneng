# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
####
ip = input("Введите IP-адрес в формате '10.0.1.1': ")

f_run = 1
for oct in ip.split('.'):
	if (not oct.isdigit()) or (int(oct)<0 and int(oct)>255):
		f_run = 0

if f_run==1:
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
else:
	print('Incorrect IPv4 address')
