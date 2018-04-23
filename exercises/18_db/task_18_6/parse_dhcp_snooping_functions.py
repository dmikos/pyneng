import os
import sqlite3
import yaml
import re
from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = now - timedelta(days=7)


def create_db(db_fname, schema_fname):
    db_exists = os.path.exists(db_fname)
    conn = sqlite3.connect(db_fname)

    if not db_exists:
        print('Creating schema...')
        with open(schema_fname, 'r') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Done')
    else:
        print('Database exists, assume dhcp table does, too.')


def check_db(db_fname):
    db_exists = os.path.exists(db_fname)
    return db_exists

def add_data_switches(db_fname, switches_yaml_fname):
    with open(switches_yaml_fname[0]) as f:
        data = yaml.load(f)

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


def add_data(db_fname, dhcp_snoop_fnames ):
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
                        data = (match.group('mac'), match.group('ip'), match.group('vlan'), match.group('intf'), hostname, 1, now)
                        try:
                            with conn:
                                query = '''insert into dhcp (mac, ip, vlan, interface, switch, active, last_active) values (?, ?, ?, ?, ?, ?, ?)'''
                                conn.execute(query, data)
                        except sqlite3.IntegrityError as e:
                            print('Error occured: ', e)
                            conn.execute('update dhcp set active = 1 where mac = :mac', {'mac': match.group('mac')})
                            conn.execute('update dhcp set last_active = :now where mac = :mac', {'mac': match.group('mac'), 'now': now})
                            conn.commit()

        conn.close()
    else:
        print("You need create DB first")


def get_data(db_filename, key, value):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row

    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    keys.remove(key)
    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)
    query = 'select * from dhcp where {} = ?'.format( key )
    result = conn.execute(query, (value,))

    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)


def get_all_data(db_filename):
    conn = sqlite3.connect(db_filename)
    conn.row_factory = sqlite3.Row

    print('-' * 80)
    query = 'select * from dhcp'
    result = conn.execute(query)
    for row in result:
        print('{:20} {:16} {:7} {:20} {:5} {}'.format(*row))
