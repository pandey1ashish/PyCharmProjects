#! /usr/bin/python3

import sqlite3
conn = sqlite3.connect('testDb.db')
print('Conn success!')
cursor = conn.execute("select 121, 'Ashish'")
#cursor = conn.execute("SELECT name FROM TEST.sqlite_master WHERE type='table' ORDER BY name")
#"select col_id, col_name from sample_table")
print('Query executed....')
for row in cursor:
    print(row[0])
    print('Name => ',row[1])
conn.close()
