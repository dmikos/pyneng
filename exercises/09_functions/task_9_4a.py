# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return not any(word in command for word in ignore)
####
def generate_dict_from_config(config_file):
    with open(config_file) as f:
        res_dict = {}
        for line in f:
            line = line.rstrip()
            if check_ignore(line, '!') and check_ignore(line, ignore):
                if line.startswith('  '):
                    line = line.lstrip()
                    if type(res_dict[top_one]) == type(list()):
                        tmp_list = res_dict[top_one]
                        res_dict[top_one] = {}
                        for elem in tmp_list:
                            res_dict[top_one][elem] = []
                        res_dict[top_one][top_two] = [line]
                    elif type(res_dict[top_one]) == type(dict()):
                        res_dict[top_one][top_two].append(line)
                elif line[0]==' ' and line[1]!=' ':
                  top_two = line.lstrip()
                  res_dict[top_one].append(top_two)
                else:
                    top_one = line.lstrip()
                    res_dict[top_one]=[]
    return res_dict

res = generate_dict_from_config('config_r1.txt')
for key, value in res.items():
    print('{} = {}'.format(key, value))
