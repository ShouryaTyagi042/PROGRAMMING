t = int(input())
for i in range(t) :
    l = list(map(int, input().rstrip().split()))
    total = 2*(l[0]+180)
    left = l[1]+ l[2]
    ans = total - left
    print(ans)
