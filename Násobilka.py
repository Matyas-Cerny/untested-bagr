x = int(input("Maximalni cislo a prosim:"))+1
y = int(input("Maximalni cislo b prosim:"))+1
a = 1
b = 1

while a < x:
	c = 0
	c = a * b
	print("%s X %s = %s" % (a, b, c))
	b += 1
	if b == y:
		a += 1
		b = 1
		print("")
	else:
		continue
