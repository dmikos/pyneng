# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''

import glob
import os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)
####
import sqlite3


def check_db(db_fname):
    db_exists = os.path.exists(db_fname)
    return db_exists

# def switches_table_update(db_fname, switches_yaml_fname):
def switches_table_update():
    db_fname = 'dhcp_snooping.db'
    switches_yaml_fname = 'switches.yml'

    import yaml

    with open(switches_yaml_fname) as f:
        data = yaml.load(f)
    #print(data['switches'])

    if check_db(db_fname):
        conn = sqlite3.connect(db_fname)

        for hostname, location in data['switches'].items():
            try:
                with conn:
                    query = '''insert into switches (hostname, location) values (?, ?)'''
                    conn.execute(query, (hostname, location))
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

        conn.close()
    else:
        print("You need create DB first")


#def dhcp_table_update(db_fname, dhcp_snoop_fnames):
def dhcp_table_update():
    import glob
    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    db_fname = 'dhcp_snooping.db'
    dhcp_snoop_fnames = dhcp_snoop_files

    import re

    if check_db(db_fname):
        conn = sqlite3.connect(db_fname)

        conn.execute('update dhcp set active = 0')
        conn.commit()

        for fname in dhcp_snoop_fnames:
            hostname = fname.split('_')[0]
            with open(fname) as f:
                for row in f.readlines():
                    match = re.search('(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<intf>\S+)', row)
                    if match:
                        data = (match.group('mac'), match.group('ip'), match.group('vlan'), match.group('intf'), hostname, 1)
                        try:
                            with conn:
                                query = '''insert into dhcp (mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, ?)'''
                                conn.execute(query, data)
                        except sqlite3.IntegrityError as e:
                            print('Error occured: ', e)
                            # print(match.group('mac'))
                            conn.execute('update dhcp set active = 1 where mac = :mac', {'mac': match.group('mac')})
                            conn.commit()

        conn.close()
    else:
        print("You need create DB first")


if __name__=="__main__":
    #switches_table_update(db_filename, 'switches.yml')
    #dhcp_table_update(db_filename, dhcp_snoop_files)
    
    switches_table_update()
    dhcp_table_update()
