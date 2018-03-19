a = 1
b = 1
while a < 1100000:
	c = 0
	c = a * b
	print("%s X %s is %s" % (a, b, c))
	b += 1
	if b == 110000:
		a += 1
		b = 1
		print("")
	else:
		continue
