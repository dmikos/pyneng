# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, 
* в виде списка (пробелы в начале строки можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return not any(word in command for word in ignore)
####
def generate_dict_from_config(config_file):
    with open(config_file) as f:
        res_dict = {}
        for line in f:
            line = line.rstrip()
            if ignore_command(line, '!') and ignore_command(line, ignore):
                if line.startswith(' '):
                    res_dict[top_command].append(line)
                    #print(res_dict[top_command])
                    #print(top_command)
                    #print(line)
                else:
                    top_command = line
                    res_dict[top_command]=[]
                    #print(res_dict[line])

    return res_dict

res = generate_dict_from_config('config_sw1.txt')
for key, value in res.items():
    print('{} = {}'.format(key, value))
