# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
import yaml

def convert_topology_dict(topology_dict):
    converted_dict={}
    for device, value in topology_dict.items():
        #print("key-{}, value-{}".format(key, value))
        for local_intf, value1 in value.items():
            for device_id, port_id in value1.items():
                # print("Device={}, Local interface={}, Device ID={}, Port ID={}".format(device, local_intf, device_id, port_id))
                converted_dict.update({(device, local_intf):(device_id, port_id)})

    #print(converted_dict)
    return converted_dict

with open('topology.yaml') as f:
    topology_dict = yaml.load(f)
# print(topology_dict)

converted_dict = convert_topology_dict(topology_dict)
draw_topology(converted_dict, out_filename='task_17_2c.svg')

#draw_topology(topology_dict, out_filename='task_17_2c.svg')
# test_dict = {('R1', 'Eth 0/0'): ('SW1', 'Eth 0/1'), ('R2', 'Eth 0/0'): ('SW1', 'Eth 0/2'), ('R2', 'Eth 0/1'): ('R5', 'Eth 0/0'), ('R2', 'Eth 0/2'): ('R6', 'Eth 0/1'), ('R3', 'Eth 0/0'): ('SW1', 'Eth 0/3'), ('R4', 'Eth 0/0'): ('SW1', 'Eth 0/4'), ('R4', 'Eth 0/1'): ('R5', 'Eth 0/1'), ('R5', 'Eth 0/0'): ('R2', 'Eth 0/1'), ('R5', 'Eth 0/1'): ('R4', 'Eth 0/1'), ('R6', 'Eth 0/1'): ('R2', 'Eth 0/2'), ('SW1', 'Eth 0/1'): ('R1', 'Eth 0/0'), ('SW1', 'Eth 0/2'): ('R2', 'Eth 0/0'), ('SW1', 'Eth 0/3'): ('R3', 'Eth 0/0'), ('SW1', 'Eth 0/4'): ('R4', 'Eth 0/0')}
# draw_topology(test_dict)
