#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sqlite3
from collections import Iterable

def by_id(t):
	return int(t[0])

try:
	conn = sqlite3.connect('c:\\workspace\\test.db')
	cursor = conn.cursor()
	print('connect success!')
except:
	print('connect error!')

try:
	#pass
	cursor.execute('insert into user (id, name) values (\'4\',\'Harry\')')
	print('insert rows: %d.' % cursor.rowcount)
except:
	print('insert failure!')
finally:
	cursor.close()
	conn.commit()
	conn.close()

try:
	conn = sqlite3.connect('c:\\workspace\\test.db')
	cursor = conn.cursor()
	print('connect success!')
except:
	print('connect error!')

try:
	#pass
	cursor.execute('select * from user')
	values = cursor.fetchall()
	print('query success!')
	if isinstance(values, Iterable):
		print('values is Iterable.')
		for id, name in sorted(values,key=by_id):
			print('ID = %s, NAME = %s.' % (id,name))
except:
	print('query failure!')
finally:
	cursor.close()
	conn.commit()
	conn.close()