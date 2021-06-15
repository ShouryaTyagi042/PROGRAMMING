a = int(input())
l = []
for i in range(0, a):
    b = str(input())
    sum_ = int(b[0]) + int(b[len(b) - 1])
    l.append(sum_)
for ch in l:
    print(ch)
