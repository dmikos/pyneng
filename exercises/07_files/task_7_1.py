# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
####
ospf_route_template = '''Protocol:\t\tOSPF
Prefix:\t\t\t{1}
AD/Metric:\t\t{2}
Next-Hop:\t\t{4}
Last update:\t\t{5}
Outbound Interface\t{6}'''

with open('ospf.txt', 'r') as f:
	for line in f:
		print(ospf_route_template.format(*line.split()))
		print()
