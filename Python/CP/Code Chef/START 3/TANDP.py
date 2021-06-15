t = int(input())
for i in range(t):
    arr_1 = tuple(map(int, input().rstrip().split()))
    arr_2 = tuple(map(int, input().rstrip().split()))
    arr_3 = tuple(map(int, input().rstrip().split()))
    tm = abs(arr_1[0] - arr_2[0] + arr_1[1] - arr_2[1])
    pm = max(arr_1[0] - arr_3[0], arr_1[1] - arr_3[1])
    if tm > pm:
        print("NO")
    elif pm > tm or pm == tm:
        print("YES")
