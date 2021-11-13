txt = input()
l = txt.split()
l1 = []
for i in l :
    l1.append(len(i))
print(l[l1.index(max(l1))])

