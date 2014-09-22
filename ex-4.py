s = "abc"
sum = 0
for i in s:
	sum += ord(i)
print sum
b = []
for i in s:
	b.append(ord(i))
print b
a = map(ord,s)
print a