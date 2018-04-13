# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
####
def parse_cdp_neighbors(local_id, show_cdp_neighbors):
    
    res = dict()
    flag = False

    for line in show_cdp_neighbors.split('\n'):
        if flag and line:
            list_line = line.split()
            device_id = list_line[0]

            if '/' in list_line[1]:
                local_intf = list_line[1]
            else:
                local_intf = list_line[1]+list_line[2]
            
            try:
                int(list_line[-1][0])
            except ValueError:
                port_id = list_line[-1]
            else:
                port_id = list_line[-2]+list_line[-1]

            # print("Device ID = {}, Local Intrfce = {}, Port ID = {}".format(device_id, local_intf, port_id))
            res[(local_id,local_intf)] = (device_id, port_id)
            # print(res)

        elif line.startswith('Device'):
            flag = True
    return res


if __name__ == "__main__":
    with open("sw1_sh_cdp_neighbors.txt") as f:
        content = f.read()
    
    print(parse_cdp_neighbors('SW1', content))
