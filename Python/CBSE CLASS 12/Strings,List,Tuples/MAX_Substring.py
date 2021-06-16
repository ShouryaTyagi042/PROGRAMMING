str1 = "Hello Pyhton sgb"
words = str1.split(" ")
maxl = 0
maxw = ""
for i in words :
    x = len(i)
    if x > maxl and i.isalpha() == True :
        print(i)
        maxl = x
        maxw = i
print(maxw)
