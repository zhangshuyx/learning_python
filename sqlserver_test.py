#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, pyodbc
from collections import Iterable

def by_id(t):
	return int(t[0])

try:
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=BASE;UID=sa;PWD=tmcsoft')
	cursor = conn.cursor()
	print('connect success!')
except:
	print('connect error!')

try:
	pass
	#cursor.execute('create table dbo.user_id_name(id varchar(20) primary key, name varchar(20))')
	#print('create table user_id_name success!')
except:
	print('create table user_id_name failure!')

try:
	#pass
	cursor.execute('insert into dbo.user_id_name (id, name) values (\'3\',\'Mary\')')
	print('insert rows: %d.' % cursor.rowcount)
except:
	print('insert failure!')
finally:
	cursor.close()
	conn.commit()
	conn.close()

try:
	conn = pyodbc.connect('DRIVER={SQL Server};SERVER=127.0.0.1;DATABASE=BASE;UID=sa;PWD=tmcsoft')
	cursor = conn.cursor()
	print('\nconnect success!')
except:
	print('\nconnect error!')

try:
	#pass
	cursor.execute('select * from dbo.user_id_name')
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