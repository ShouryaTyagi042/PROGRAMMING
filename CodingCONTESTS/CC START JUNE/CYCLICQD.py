t = int(input())
for i in range(t) :
    l = list(map(int, input().rstrip().split()))
    if l[0]+l[2] == 180 and l[1] + l[3] == 180 :
        print("YES")
    else :
        print('NO')
