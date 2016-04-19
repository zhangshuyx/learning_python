#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

doc = xml.dom.minidom.parse("c:\\TDdownload\\MRO\\test.xml")
bulkPmMrDataFile = doc.documentElement

enbs = bulkPmMrDataFile.getElementsByTagName("eNB")
print("*****eNB*****")
#if enbs[0].hasAttribute("id"):
	#print ("eNB id: %s" % enbs[0].getAttribute("id"))
measurements = enbs[0].getElementsByTagName("measurement")
for measurement in measurements:
	print("*****measurement*****")
	#if measurement.hasAttribute("id"):
		#print ("eNB id: %s" % measurement.getAttribute("id"))
	smrs = measurement.getElementsByTagName("smr")
	print("*****smr*****")
	print(smrs[0].childNodes[0].data)  #获取文本值
	objects = measurement.getElementsByTagName("object")
	for object in objects:
		#print("*****object*****")
		vs = object.getElementsByTagName("v")
		for v in vs:
			print("*****v*****")
			print(enbs[0].getAttribute("id")+' '+object.getAttribute("id")+' '+object.getAttribute("MmeUeS1apId")+' '+object.getAttribute("MmeGroupId")+' '+object.getAttribute("MmeCode")+' '+object.getAttribute("TimeStamp")+' '+v.childNodes[0].data)  #获取文本值

