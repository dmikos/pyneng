# -*- coding: utf-8 -*-
"""
Задание 18.1

create_db.py
* сюда должна быть вынесена функциональность по созданию БД:
 * должна выполняться проверка наличия файла БД
 * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
   должна быть создана БД (БД отличается от примера в разделе)

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
"""

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
####
import sqlite3
import os

#def check_create_db(db_fname, schema_fname):
def check_create_db():
    db_fname = db_filename
    schema_fname = schema_filename
    
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

if __name__=="__main__":
    #check_create_db(db_filename, schema_filename)
    check_create_db()