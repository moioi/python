# -*- coding:  utf-8 -*-
import re
openFile = open('bo.moioi.com.log','r')
baiduspiderFile = open('baiduspider.log','w')

wholeFile = openFile.readlines()
for line in wholeFile:
	if re.search(r"Baiduspider",line):
		reg = re.compile('^(?P<remote_ip>[^ ]+) (?P<no1>[^ ]*) (?P<no2>[^ ]*) (?P<date1>[^ ]*) (?P<date2>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')
		regMatch = reg.search(line)
		linebits = regMatch.groupdict()
		print linebits
		for k, v in linebits.items():
    			print k+": "+v
    			
		# print line
	else:
		pass
	# ss = line.find(r"Baiduspider")
	# if ss >= 1:
	# 	print line
	# 	baiduspiderFile.write(line)
	# else:
	# 	pass
	# re.search,find都可以查找字符串
openFile.close()
baiduspiderFile.close()

