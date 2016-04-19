#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import xml.dom.minidom
from xml.dom.minidom import parse
from os.path import join, splitext

#读入XML文档
doc = xml.dom.minidom.parse("c:\\TDdownload\\MRO\\TD-LTE_MRO_NSN_OMC_122941_20160222200000.xml")
bulkPmMrDataFile = doc.documentElement

#读入子元素
enbs = bulkPmMrDataFile.getElementsByTagName("eNB")
measurements = enbs[0].getElementsByTagName("measurement")
objects = measurements[0].getElementsByTagName("object")

s = ''
with open('C:\\TDdownload\\MRO\\TD-LTE_MRO_NSN_OMC_122941_20160222200000.csv','w') as t:		#生成csv文件以写入数据
	for object in objects:
		vs = object.getElementsByTagName("v")
		for v in vs:
			s = s +(enbs[0].getAttribute("id")+' '+object.getAttribute("id")+' '+object.getAttribute("MmeUeS1apId")+' '+object.getAttribute("MmeGroupId")+' '+object.getAttribute("MmeCode")+' '+object.getAttribute("TimeStamp")+' '+v.childNodes[0].data+'\n')  #获取文本值
	t.writelines((((s.replace(' \n','\n')).replace(' ',',')).replace('T',' ')).replace('NIL',''))	#写入解析后内容
	#t.writelines(s)