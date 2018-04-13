# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''
####
import subprocess


def check_ip_addresses(ip_addresses):
    ip_list_true=[]
    ip_list_false=[]
    
    if '-' in ip_addresses[0]:
        ip_addresses_list = ip_addresses[0].split('-')
        ip_begin = ip_addresses_list[0]
        ip_begin_split = ip_begin.split('.')
        ip_end = ip_addresses_list[1]

        ip_main = ip_begin_split[:-1]
        ip_f = ip_begin_split[-1]
        ip_s = ip_end.split('.')[-1]
        ip_main_join = ('.').join(ip_main)
        ip_addresses_func = [ip_main_join+'.'+str(ip) for ip in range(int(ip_f), int(ip_s)+1)]
    else:
        ip_addresses_func = ip_addresses

    #print(ip_addresses_func)


    for ip_address in ip_addresses_func:
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
    # ip_list = ['8.8.8.8', 'a', '10.0.0.1', '8.8.8.4', '192.168.1.1', '192.168.1.4']
    # ip_list = ['10.1.1.1']
    # ip_list = ['10.1.1.1-10.1.1.3']
    ip_list = ['10.1.1.1-3']
    result = check_ip_addresses(ip_list)
    print("IP_true = {}, IP_false = {}".format(result[0], result[1]))
