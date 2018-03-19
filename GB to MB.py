x = 0
while True:
    try:
	    x = int(input("Paměť v GB:"))
	    break
    except Exception as e:
	    print("Ty seš ale šťastlivec, dostal jsi chybu. Jako dárek tady máš error kód:", e)
	    continue
mem = x *1024
print(mem)
