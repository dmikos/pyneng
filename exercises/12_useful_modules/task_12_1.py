# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
####
import subprocess


def check_ip_addresses(ip_addresses):
    ip_list_true=[]
    ip_list_false=[]
    
    for ip_address in ip_addresses:
        reply = subprocess.run(['ping', '-c', '3', '-n', ip_address],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL,
                               encoding='utf-8')
        
        if reply.returncode == 0:
            ip_list_true.append(ip_address)
        else:
            ip_list_false.append(ip_address)

    return ip_list_true, ip_list_false

if __name__ == "__main__":
    ip_list = ['8.8.8.8', 'a', '10.0.0.1', '8.8.8.4', '192.168.1.1', '192.168.1.4']
    result = check_ip_addresses(ip_list)
    print("IP_true = {}, IP_false = {}".format(result[0], result[1]))
