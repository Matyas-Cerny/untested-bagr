x = 0
while True:
    try:
	    x = int(input("Kolik mi dáš čísel:"))
	    break
    except Exception as e:
	    print("Ty seš ale šťastlivec, dostal jsi chybu. Jako dárek tady máš error kód:", e)
	    continue
cisla = []
for i in range(x):
	cisla.append(int(input("Dej mi číslo")))
y = cisla[0]
for i in cisla:
	if i < y:
		y = i
print (y)
print("Tvůj vstup:",cisla)
