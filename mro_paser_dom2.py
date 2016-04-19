#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import csv
import xml.dom.minidom
from xml.dom.minidom import parse
from os.path import join, splitext

#读入XML文档
doc = xml.dom.minidom.parse("c:\\TDdownload\\MRO\\test.xml")
bulkPmMrDataFile = doc.documentElement

#读入子元素
enbs = bulkPmMrDataFile.getElementsByTagName("eNB")
measurements = enbs[0].getElementsByTagName("measurement")
objects = measurements[0].getElementsByTagName("object")

s = []
with open('C:\\TDdownload\\MRO\\test2.csv','w') as t:		#生成csv文件以写入数据
	swriter = csv.writer(t,dialect='excel')
	for object in objects:
		vs = object.getElementsByTagName("v")
		for v in vs:
			swriter.writerow('['+enbs[0].getAttribute("id")+','+object.getAttribute("id")+','+object.getAttribute("MmeUeS1apId")+','+object.getAttribute("MmeGroupId")+','+object.getAttribute("MmeCode")+','+object.getAttribute("TimeStamp")+','+v.childNodes[0].data.rstrip().replace(' ',',')+']')  #获取文本值
			
			#print(s)
	#t.writelines((((s.replace(' \n','\n')).replace(' ',',')).replace('T',' ')).replace('NIL',''))	#写入解析后内容
	#t.writelines(s)
	