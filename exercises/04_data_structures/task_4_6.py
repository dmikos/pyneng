# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
####
ospf_route_val = ospf_route.split()

ospf_route_template = '''Protocol:\t\tOSPF
Prefix:\t\t\t{1}
AD/Metric:\t\t{2}
Next-Hop:\t\t{4}
Last update:\t\t{5}
Outbound Interface\t{6}'''

print(str(ospf_route_template).format(*ospf_route_val))

