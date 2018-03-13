# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
####
ip = input("Введите IP-адрес в формате '10.0.1.1': ")
#ip='12.168.2.3'
#ip='192.168.2.3'
#ip='132.168.2.3'
#ip='230.168.2.3'
#ip='255.255.255.255'
#ip='255.255.4.255'
#ip='0.0.0.0'


# oct1,oct2, oct3, oct4 = ip.split('.')
oct1,oct2, oct3, oct4 = [int(x) for x in ip.split('.')]
print("ip={}, oct1={}, oct2={}, oct3={}, oct4={}".format(ip, oct1, oct2, oct3, oct4))

# oct1, oct2, oct3, oct4 = int(oct1), int(oct2), int(oct3), int(oct4) 

if oct1 >= 1 and oct1 <= 223:
	print('unicast')
elif oct1 >= 224 and oct1 <= 239:
	print('multicast')
#elif oct1==255 and oct2==255 and oct3==255 and oct4==255:
elif oct1==oct2==oct3==oct4==255:
	print('local broadcast')
#elif oct1==0 and oct2==0 and oct3==0 and oct4==0:
elif oct1==oct2==oct3==oct4==0:
	print('unassigned')
else:
	print('unused')
