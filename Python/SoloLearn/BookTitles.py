file = open("/usercode/files/books.txt", "r")

for var in file.readlines() :
    f = len(var.rstrip("\n"))
    print(var[0]+str(f))




file.close()
