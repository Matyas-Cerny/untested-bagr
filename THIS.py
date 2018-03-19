a = int(input("Číslo 1 prosím."))
b = int(input("Číslo 2 prosím."))
c = int(input("Číslo 3 prosím."))
if a < b < c:
	print (a, b, c)
elif a < c < b:
	print (b, c, a)
elif c < b < a:
	print (c, b ,a)
elif c < a < b:
	print (c, a, b)
elif b < a <c:
	print (b, a, c)
else:
	print (b, c, a)
print ("Dobrou noc")
