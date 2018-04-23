# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. 
 * Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import sqlite3
import yaml


db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)
####


# def switches_table_update(db_fname, switches_yaml_fname):
def switches_table_update():
    db_fname = 'dhcp_snooping.db'
    switches_yaml_fname = 'switches.yml'


    with open(switches_yaml_fname) as f:
        data = yaml.load(f)
    #print(data['switches'])

    conn = sqlite3.connect(db_fname)

    for hostname, location in data['switches'].items():
        try:
            with conn:
                query = '''insert into switches (hostname, location) values (?, ?)'''
                conn.execute(query, (hostname, location))
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)

    conn.close()


#def dhcp_table_update(db_fname, dhcp_snoop_fnames):
def dhcp_table_update():
    db_fname = 'dhcp_snooping.db'
    dhcp_snoop_fnames = dhcp_snoop_files

    import re

    conn = sqlite3.connect(db_fname)

    for fname in dhcp_snoop_fnames:
        hostname = fname.split('_')[0]
        with open(fname) as f:
            for row in f.readlines():
                match = re.search('(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)', row)
                if match:
                    data = (match.group('mac'), match.group('ip'), match.group('vlan'), match.group('intf'), hostname)
                    try:
                        with conn:
                            query = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
                            conn.execute(query, data)
                    except sqlite3.IntegrityError as e:
                        print('Error occured: ', e)
    conn.close()



if __name__=="__main__":
    #switches_table_update(db_filename, 'switches.yml')
    #dhcp_table_update(db_filename, dhcp_snoop_files)
    switches_table_update()
    dhcp_table_update()
