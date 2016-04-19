#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#本脚本完成MRO_XML文件转换为可入库的csv文件
import os
from xml.parsers.expat import ParserCreate
from os.path import join, splitext

#变量声明
d_eNB = {}
d_obj = {}
s = ''
flag = True

#Sax解析类
class DefaultSaxHandler(object):
	#处理开始标签
	def start_element(self, name, attrs):
		global d_eNB
		global d_obj
		global s
		if name == 'bulkPmMrDataFile':
			pass
		elif name == 'fileHeader':
			pass
		elif name == 'eNB':
			d_eNB = attrs
		elif name == 'measurement':
			pass
		elif name == 'smr':
			pass
		elif name == 'object':
			d_obj = attrs
		elif name == 'v':
			s = s + d_eNB['id']+' '+ d_obj['id']+' '+d_obj['MmeUeS1apId']+' '+d_obj['MmeGroupId']+' '+d_obj['MmeCode']+' '+d_obj['TimeStamp']+' '
			pass
		else:
			pass
	#处理中间文本
	def char_data(self, text):
		global d_eNB
		global d_obj
		global s
		global flag
		if text[0:1].isnumeric():
			s = (s + text)
		elif text.startswith('MR.LteScPlrULQci1'):
			flag = False
			#print(text,flag)
		else:
			pass
	#处理结束标签
	def end_element(self, name):
		global d_eNB
		global d_obj
		global s
		if name == 'object':
			pass
		elif name == 'v':
			s = s + '\n'
		else:
			pass

#Sax解析调用
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

#
with open('C:\\TDdownload\\MRO\\TD-LTE_MRO_NSN_OMC_122941_20160222200000.csv','w') as t:		#生成csv文件以写入数据
	with open('C:\\TDdownload\\MRO\\TD-LTE_MRO_NSN_OMC_122941_20160222200000.xml','r') as f:		#打开xml文件读取内容
		for line in f.readlines():
			if flag:
				parser.Parse(line) #解析xml文件内容
			else:
				break
	t.writelines(s.replace(' \n','\r\n').replace(' ',',').replace('T',' ').replace('NIL',''))	#写入解析后内容

