storage=[]
filename = "DatList.txt"
while True:
    print("""
1)Create an entry.
2)List all entries.
3)Write to file.
4)Read from file.
5)Find an entry
""")
    inpt = int(input("Select:"))
    if inpt == 1:
        name = "Name: " + input("Name: ")
        phone = "Phone: " + input("Phone: ")
        storage.append(name)
        storage.append(phone)
    elif inpt == 2:
        print("\n")
        for i in range(int(len(storage)/2)):
            print(storage[i*2], storage[i*2+1])
        inpt = input("Press return to continue.")
    elif inpt == 3:
        lst = "\n"
        lst = lst.join(storage)
        fh = open(filename,  mode="w", encoding="utf-8")
        fh.write(lst)
        fh.close()
        print("written \n")
    elif inpt == 4:
        storage =[]
        file = open(filename)
        for i in file:
            storage.append(i.strip())
        print("Loaded")
    elif inpt == 5:
        inpt = input("Ask Jeeves:")
        for i in range(len(storage)):
            if inpt in storage[i]:
                if i%2 == 0:
                    print(storage[i])
                    print(storage[i+1])
                else:
                    print(storage[i-1])
                    print(storage[i])
                print("\n")
                inpt = input("Press return to continue.")
