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
mysla = [] 
mysla.append(cisla[0])
kysla = []
y = 0
z = 1 
while z < x:
    if cisla[y] < cisla[z]:
        mysla.append(cisla[z])
    else :
        print ("O-OU CHYBA! Zde máš to co máš správně", mysla,)
        stop = 0
        for i in range(z):
            if mysla[i] >cisla[z] and stop < 1:
                kysla.append(cisla[z])
                stop = 1
            kysla.append(mysla[i])
        mysla = kysla
        kysla = []
    z += 1
    y += 1
if z == x:
    print("V poho je to po vzestupně")
print("Tvůj vstup:",cisla)
print (mysla)
