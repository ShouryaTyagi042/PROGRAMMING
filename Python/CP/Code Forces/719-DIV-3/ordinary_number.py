l = int(input())
for i in range(l) :
    x = int(input())
    ans = 0
    for j in range(1,x+1) :
        str1 = str(j)
        flag = True
        for k in range(len(str1)) :
            if str1[0] != str1[k] :
                flag = False
                break
        if flag == True :
            ans += 1
    print(ans)
