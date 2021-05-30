t = int(input())
for i in range(t):
    arr = set(map(int, input().rstrip().split()))
    if arr[0] >= arr[2] * arr[4] and arr[1] >= arr[3] * arr[4]:
        print("YES")
    else:
        print("NO")
