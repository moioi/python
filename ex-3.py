a = {'a':1,'b':2,'c':3,'d':4}
i = a.keys()
# for item in a.keys():
# 	i.append(item)
# 	print "%s:%s" % (item, a[item])

i.sort()
print i
for d in i:
	print "%s:%s" %(d, a[d])