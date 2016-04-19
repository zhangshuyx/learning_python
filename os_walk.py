#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
from os.path import join, splitext, abspath, basename

xmls = []
for root, dirs, files in os.walk(r'C:\TDdownload\MRO'):
	for file in files:
		if os.path.splitext(file)[1] == '.xml':
			xmls.append(os.path.join(root,file))
for xml in xmls:
	print(xml)
	print(os.path.basename(xml))
