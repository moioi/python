# -*- coding:  utf-8 -*-
openFile = open('test.txt','r')
s = openFile.readlines()
for line in s:
	print line
print s
length = 0
for item in s:
	length += len(item.decode('utf-8'))
	print item.replace('2012','2013')
	print item.replace('\n','')
print length
