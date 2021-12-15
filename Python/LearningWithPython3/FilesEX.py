fh = open("snakes.txt",'r')
fh2 = open("reversed.txt","w")
fh3 = open("snakes_test.txt","w")


def reversed_order() :
    data = fh.readlines()
    # print(data)
    no_lines = len(data)-1
    i = no_lines
    while i >= 0 :
        fh2.write(data[i])
        i -= 1
reversed_order()

def snakes_test() :
    data = fh.readlines()
    print(data)
    for i in data :
        if "snakes" in i :
            fh3.write(i)
snakes_test()
