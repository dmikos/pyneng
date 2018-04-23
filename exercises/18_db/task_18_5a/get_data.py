# -*- coding: utf-8 -*-
####
import sqlite3
import sys

db_filename = 'dhcp_snooping.db'
keys = ['mac', 'ip', 'vlan', 'interface', 'switch']

def check_args():
    if len(sys.argv) == 3:
        col, val = sys.argv[1:]
        if col not in keys:
            print('Данный параметр не поддерживается.\nДопустимые значения параметров: mac, ip, vlan, interface, switch')
            exit(1)
        return col, val
    elif len(sys.argv) == 1:
        return 'dhcp'
    else:
        print("Пожалуйста, введите два или ноль аргументов")


def print_from_table(data):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row
    
    if isinstance(data, str):
        print('We have this information in dhcp table')
        print('-' * 40)
        print('Active values:')
        print('-' * 40)

        query = 'select * from dhcp where active=1'
        result = conn.execute(query)
        for row in result:
            print('{:20} {:16} {:7} {:20} {:5} {}'.format(*row))
        
        print('-' * 40)
        print('Inactive values:')
        print('-' * 40)

        query = 'select * from dhcp where active=0'
        result = conn.execute(query)
        for row in result:
            print('{:20} {:16} {:7} {:20} {:5} {}'.format(*row))



    elif isinstance(data, tuple):
        key, value = data
        keys.remove(key)
        print('\nDetailed information for host(s) with', key, value)
        print('-' * 40)
        query = 'select * from dhcp where {} = ? and active = 1'.format( key )
        result = conn.execute(query, (value,))

        for row in result:
            for k in keys:
                print('{:12}: {}'.format(k, row[k]))
            print('-' * 40)

        print('-' * 40)
        print('Inactive values:')
        print('-' * 40)
        query = 'select * from dhcp where {} = ? and active = 0'.format( key )
        result = conn.execute(query, (value,))

        for row in result:
            for k in keys:
                print('{:12}: {}'.format(k, row[k]))
            print('-' * 40)


if __name__=="__main__":
    result = check_args()
    print_from_table(result)
